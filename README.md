![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Latest-orange.svg)
![XGBoost](https://img.shields.io/badge/XGBoost-Optimized-green.svg)
![Optuna](https://img.shields.io/badge/Optuna-Hyperparameter_Tuning-blueviolet.svg)

## 📌 Project Overview
This repository contains an end-to-end Machine Learning project aimed at predicting real estate prices with high accuracy. The project covers the entire data science lifecycle: from raw data extraction, comprehensive data cleaning, and feature engineering to handling highly skewed target variables and advanced hyperparameter tuning using **Optuna**.

The final optimized **XGBoost** model achieved an outstanding **$R^2$ score of 0.92**, significantly reducing the real-world prediction error (MAE) compared to baseline models.

## 🚀 Key Highlights & Methodology

1. **Data Preprocessing & Cleaning (`cleandata.ipynb` & `src/`):**
   - Developed custom modular scripts (e.g., `persian_to_english_digits`) stored in the `src/` directory to standardize localized data formats.
   - Handled missing values, outliers, and categorical encoding.
2. **Handling Target Skewness:**
   - Real estate prices are heavily right-skewed. Applied **Logarithmic Transformation** (`np.log1p`) to the target variable before training to normalize the distribution.
   - Predictions were transformed back to the real price scale using `np.expm1` for accurate business-level error calculation (MAE, RMSE).
3. **Advanced Modeling (`training.ipynb`):**
   - **Baseline Model:** Evaluated a Linear Regression model (achieving ~$R^2 = 0.88$) to establish a strong baseline.
   - **Ensemble Methods:** Trained Random Forest and XGBoost algorithms.
4. **Hyperparameter Tuning:**
   - Utilized **Optuna** framework to systematically search the hyperparameter space (50 trials per model).
   - Optimized complex tree-based parameters such as `n_estimators`, `learning_rate`, `max_depth`, and `subsample`.

## 📊 Model Performance Comparison

The models were evaluated based on the **Real Price** scale (after reversing the log transformation). Below are the final results on unseen test data:

| Model | MAE (Real Price) | RMSE (Real Price) | $R^2$ Score |
| :--- | :--- | :--- | :--- |
| **Linear Regression** (Baseline) | - | - | ~ 0.8800 |
| **Random Forest** (Optuna Tuned) | 4,366,105,710 | 8,731,438,568 | 0.9033 |
| **XGBoost** (Optuna Tuned) 🏆 | **3,654,938,023** | **7,296,252,105** | **0.9218** |

*Note: The XGBoost model outperformed others, proving its superiority in handling tabular data and complex non-linear relationships.*

## 📂 Repository Structure
```text
├── data/                       # Contains raw and cleaned datasets 
├── src/                        # Modularized Python scripts (e.g., data formatters, cleaners)
│   ├── __init__.py
│   └── cleaning_utils.py       # Functions like persian_to_english_digits
├── cleandata.ipynb             # Jupyter Notebook for EDA and Data Preprocessing
├── training.ipynb              # Jupyter Notebook for Model Training & Optuna Tuning
├── requirements.txt            # Project dependencies
└── README.md                   # Project documentation



## ⚙️ How to Run the Project
1. **Clone the repository:**
   
```bash
git clone https://github.com/Mohammadhkabiri/Real-Estate-Valuation-ML.git

 2. **Install dependencies:Ensure you have Python installed, then run:**
```bash
   pip install -r requirements.txt

3. **Execute the Notebooks:**
Run cleandata.ipynb first to generate the cleaned dataset.
Run training.ipynb to train the models and reproduce the results.
🛠 Technologies Used
Language: Python
Libraries: Pandas, NumPy, Scikit-Learn, XGBoost, Optuna, Matplotlib, Seaborn
Environment: Jupyter Notebook
💡 Conclusion
Reaching an R^2 of 0.92 in real estate pricing is considered highly accurate, capturing the majority of variance without overfitting. This project demonstrates proficiency in standardizing messy data, applying rigorous statistical transformations, and implementing state-of-the-art machine learning optimization techniques
