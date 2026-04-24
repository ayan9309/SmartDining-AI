# 🍽️ SmartDining AI: Content-Based Restaurant Recommender

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Backend-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Machine_Learning-Scikit_Learn-orange?style=for-the-badge&logo=scikit-learn)
![UI](https://img.shields.io/badge/UI-Glassmorphism-38B2AC?style=for-the-badge)

**SmartDining AI** is an intelligent, web-based recommendation engine designed to curate personalized dining experiences in Bangalore. 

This project leverages **Natural Language Processing (NLP)** to analyze unstructured customer reviews and quantitative metrics (cuisine type, cost, ratings). By processing these features through a custom TF-IDF vectorization engine, it provides highly accurate, taste-matched restaurant recommendations instantly.

---

## 🚀 Key Features

* **⚡ Real-Time Engine:** Optimized Flask backend computes cosine similarity across thousands of data points in under 200 milliseconds.
* **🔍 Smart Auto-Complete & Fuzzy Search:** Features a dynamic, AJAX-powered search bar that fetches database matches as the user types, equipped with a fuzzy-matching fallback algorithm to prevent typo-induced crashes.
* **🧠 Advanced NLP Model:** Powered by Scikit-Learn's `TfidfVectorizer` to extract semantic meaning from customer reviews, ignoring irrelevant stop words.
* **🎨 Premium UI/UX:** A sleek, modern "Light Mode" interface featuring custom-styled data dashboards, hover states, glassmorphism, and a dynamic UI Normalization Engine to map mathematical scores to human-readable percentages.
* **📊 Pre-Trained Efficiency:** The heavy mathematical matrix is pre-compiled via Jupyter Notebook into a `.pkl` file, resulting in zero-lag user queries.

---

## 📂 Project Structure

```text
Restaurant_Recommendation_System/
│
├── Document/
│   └── RESTAURANT_RECOMMENDATION_SYSTEM.docx  # Final Project Report
│
├── Flask/
│   ├── static/                                # Custom CSS/JS assets
│   ├── templates/
│   │   ├── index.html                         # Premium landing page
│   │   ├── web.html                           # Auto-complete search interface
│   │   └── result.html                        # Formatted data output dashboard
│   │
│   ├── app1.py                                # Main Flask Web Server
│   ├── Restaurant_Recommendation_System.ipynb # Primary Training Script (EDA & Model)
│   ├── requirements.txt                       # Project Dependencies
│   │
│   │   *(Note: The following files are ignored via .gitignore due to size limits)*
│   ├── zomato.csv                             # Extracted raw dataset (Needs to be downloaded)
│   ├── restaurant.pkl                         # Trained Model Matrix (Generated via Notebook)
│   └── restaurant1.csv                        # Cleaned Dataset (Generated via Notebook)
│
└── README.md
```
## ⚙️ Installation & Setup
Important Note regarding File Sizes: Due to GitHub's 100MB file limit, the raw zomato.csv dataset and the pre-computed restaurant.pkl matrix are not included in this repository. Follow the steps below to generate them locally.

1. Clone the Repository & Install Dependencies
Ensure you have Python installed on your system. Open your terminal and run:
```git clone [https://github.com/ayan9309/SmartDining-AI.git](https://github.com/ayan9309/SmartDining-AI.git)
cd SmartDining-AI/Flask
pip install -r requirements.txt
```

2. Download the Raw Dataset
Download the "Zomato Bangalore Restaurants" dataset from Kaggle: Zomato Bangalore Dataset

Extract the .zip file.

Place the extracted zomato.csv file directly inside the Flask/ folder.

3. Generate the ML Model (Jupyter Notebook)
Before booting the web server, you must clean the raw dataset and generate the trained machine learning matrix.

Open Restaurant_Recommendation_System.ipynb using Jupyter Notebook or VS Code.

Run all cells sequentially to perform Exploratory Data Analysis (EDA) and train the NLP model.

Verify: Ensure restaurant.pkl and restaurant1.csv have successfully generated in your Flask/ folder.

4. Run the Application
Start the local server by executing the main Flask application:
``` Bash
python app1.py
```

5. Access the Interface
Open your preferred web browser and navigate to the local server address:
http://127.0.0.1:5000/

🧠 Architectural Workflow
Dynamic Input: As the user types into the interface, an AJAX request queries the backend to suggest matching restaurant names, ensuring accurate data entry.

Vectorization & Inference: Upon submission, the application loads the restaurant.pkl file, which contains a pre-computed matrix comparing the TF-IDF (Term Frequency-Inverse Document Frequency) of all restaurant reviews.

Similarity Scoring: The system identifies the index of the target restaurant and calculates the top 10 closest matches based on Cosine Similarity scores.

Data Presentation: The backend normalizes the mathematical data and renders it dynamically into a clean, modern HTML/CSS dashboard with interactive charts.

📝 License & Credits
This project is developed for educational purposes as part of the SmartInternz Artificial Intelligence Internship Program.

Designed & Developed by Mohamadayan Desai
