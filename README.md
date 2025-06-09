#🧠 Alzheimer's Disease Detection Using Various Machine Learning Algorithms


![brain](https://github.com/user-attachments/assets/b50c3ac1-f1db-477e-a8d4-ab868483d739)
## 📌 Project Overview  
This project aims to detect **Alzheimer's Disease** using **Machine Learning Models** trained on a dataset of clinical data. The feature selection entailed running six different cases on the types of features. 
- **Case 1**: The Pearson correlation finds how strongly numerical features are related to the target variable, with values ranging between -1 and 1. Features with a high positive or negative relationship are kept while weaker ones are put aside. 
- **Case 2**: All numerical features included.  
- **Case 3**: Chi-square tests measure the relationship between categorical features and the target variable using observed and expected frequencies. Those features whose chi-square statistic is above some critical threshold are retained as strongly associated with the target. This method identifies the most relevant categorical features for classification, improving model focus and predictive accuracy while reducing noise from irrelevant data.
- **Case 4**: All categorical features included.  
- **Case 5**: A combination of preselected numerical and categorical features from the previous cases.  
- **Case 6**: It contains all available features. 

## 🚀 Technologies Used  
- Python  
- Machine Learning: Logistic Regression, Decision Tree, Random Forest, Support Vector Machine (SVM), Artificial Neural Network (ANN)    
- Frameworks: TensorFlow,Scikit-Learn 
- Data Handling: Pandas, NumPy  
- Visualization: Matplotlib, Seaborn
  
## 📊 Dataset  
The dataset was sourced from **Kaggle**. We performed data preprocessing, feature selection, and model comparison to improve model performance.  

## 📈 Model Performance  
Our best-performing model achieved:  
- **Accuracy:** 95%  
- **Precision:** 96%  
- **Recall:** 96%  
- **F1-score:** 96%

