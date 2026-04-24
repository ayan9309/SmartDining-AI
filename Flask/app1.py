import pandas as pd
from flask import Flask, render_template, request, jsonify
import pickle
import warnings
import re
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load the pre-processed data and trained model
try:
    zomato_df = pd.read_csv("restaurant1.csv", encoding='utf-8')
    # TEXT SANITIZER: Automatically fix mangled Unicode characters 
    zomato_df['name'] = zomato_df['name'].apply(lambda x: re.sub(r'[^\x00-\x7F]+', "'", str(x)))
    
    df_percent = zomato_df.copy()
    df_percent.set_index('name', inplace=True)
    indices = pd.Series(df_percent.index)

    with open("restaurant.pkl", "rb") as f:
        cosine_similarities = pickle.load(f)
        
except FileNotFoundError:
    print("Error: Please run the Jupyter Notebook first to generate the model and CSV.")

# Optimized Recommendation Logic with Fuzzy Matching
def recommend(name, cosine_similarities=cosine_similarities):
    # 1. Try Exact Match First
    if name in indices.values:
        idx = indices[indices == name].index[0]
    else:
        # 2. FUZZY FALLBACK: Try Case-Insensitive Substring Match
        matches = indices[indices.str.lower().str.contains(name.lower(), na=False, regex=False)]
        if len(matches) > 0:
            idx = matches.index[0] # Grab the first closest match
        else:
            # If completely not found, return empty dataframe
            return pd.DataFrame(columns=['Error: Restaurant not found in database.'])

    score_series = pd.Series(cosine_similarities[idx]).sort_values(ascending=False)
    top_indexes = list(score_series.iloc[1:min(31, len(score_series))].index)
    top_scores = list(score_series.iloc[1:min(31, len(score_series))].values)
    
    results_data = []
    
    for i, each in enumerate(top_indexes):
        rest_name = df_percent.index[each]
        row_data = df_percent[df_percent.index == rest_name].iloc[0]
        
        results_data.append({
            'name': rest_name,
            'Cuisines': row_data['cuisines'],
            'Rating (out of 5)': row_data['Mean Rating'],
            'Cost for Two (₹)': row_data['cost'],
            'Match Score (%)': round(top_scores[i] * 100, 1) 
        })
    
    df_new = pd.DataFrame(results_data)
    df_new = df_new.drop_duplicates(subset=['Cuisines', 'Rating (out of 5)', 'Cost for Two (₹)'], keep='first')
    df_new = df_new.sort_values(by='Match Score (%)', ascending=False).head(10)
    df_new.set_index('name', inplace=True)
    
    return df_new

# --- Web Routes ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/web')
def web():
    return render_template('web.html')

@app.route('/result', methods=['POST'])
def result():
    output = request.form['output']
    res = recommend(output)
    
    html_table = res.to_html(classes='custom-table', justify='left', border=0, index=True, index_names=False)
    return render_template('result.html', keyword=html_table, search_term=output)

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    search_term = request.args.get('term', '').lower()
    if not search_term:
        return jsonify([])
        
    matches = df_percent[df_percent.index.str.lower().str.contains(search_term, na=False)].index.tolist()
    matches = sorted(list(set(matches)))
    return jsonify(matches[:10])

if __name__ == '__main__':
    app.run(debug=True)