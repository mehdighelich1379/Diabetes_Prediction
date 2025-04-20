![Screenshot 2025-04-20 194036](https://github.com/user-attachments/assets/888324d1-9872-4856-8f24-f07d465b16b3)### Medical Documentation on Diabetes Dataset


# Heart Disease Prediction
This is a machine learning model to predict heart disease based on patient data. You can interact with the app directly here:
[Try the Live App]([https://your-app-name.streamlit.app](https://diabetesprediction-with-machin-learning-mehdighelich1.streamlit.app/))


1) ## Dataset Overview:
The diabetes.csv dataset is designed to predict whether an individual has diabetes or not based on various features related to their medical history, physical conditions, and other relevant factors. This dataset is often used in machine learning applications for classification tasks. The primary goal of this project is to predict the Outcome column (whether the individual is diabetic or not) based on the other features.

2) ## Columns in the Dataset:

1. Pregnancies: The number of pregnancies the individual has had. This feature can provide insight into how pregnancy history may influence the likelihood of developing diabetes.
2. Glucose: The glucose concentration in the blood. High glucose levels are a key indicator of diabetes. Elevated glucose levels can indicate insulin resistance, which is a critical factor in type 2 diabetes.
3. BloodPressure: The blood pressure reading (in mm Hg). High blood pressure is often associated with diabetes and is considered one of the risk factors for developing the condition.
4. SkinThickness: The thickness of the skin fold, which is measured as an indicator of body fat. Excess fat can indicate insulin resistance, which can lead to type 2 diabetes.
5. Insulin: The level of insulin in the blood. Insulin resistance, where the body does not respond effectively to insulin, is a hallmark of type 2 diabetes.
6. BMI (Body Mass Index): A measure of body fat based on height and weight. Overweight individuals are at a higher risk of developing diabetes, and a higher BMI is often a precursor to type 2 diabetes.
7. DiabetesPedigreeFunction: This feature indicates the family history of diabetes. A higher score suggests a genetic predisposition to diabetes.
8. Age: The age of the individual. As age increases, the likelihood of developing diabetes tends to rise.
9. Outcome: The target variable, where 1 indicates the individual has diabetes, and 0 means they do not.

3) ## Data Analysis (Exploratory Data Analysis - EDA):

1. Initial Data Exploration: The first step in the project was performing exploratory data analysis (EDA) to understand the dataset's structure and the distribution of each feature.
2. Missing Values: The dataset contained missing values (NaN), which were imputed with the mean of the respective columns to ensure that the dataset is complete for model training.
3. Visualization: The relationships between the features and the target variable (Outcome) were visualized using various plots to gain deeper insights into the data, such as histograms, box plots, and scatter plots.
   
4) ## Data Preprocessing:

1. Scaling with MinMaxScaler: To ensure that all features are on the same scale (important for many machine learning models), the MinMaxScaler technique was applied. This technique scales the data into a range between 0 and 1.
2. Noise Removal: Outliers and noisy data were removed using the Local Outlier Factor (LOF) algorithm. LOF is an unsupervised anomaly detection algorithm that helps identify data points that deviate significantly from the rest of the data.
3. Handling Imbalanced Data: Since the dataset was imbalanced (the number of positive cases of diabetes was much lower than the negative cases), the SMOTETomek technique was applied. This combines SMOTE (Synthetic Minority Over-sampling Technique) for oversampling the minority class and Tomek Links for cleaning up the majority class, resulting in a balanced dataset.
4. Train-Test Split: The dataset was split into a training set (70%) and a testing set (30%) for model evaluation.

5) ## Model Building:

1. CatBoost Model: 
   - The first model used was CatBoost, a powerful gradient boosting algorithm. Hyperparameters such as learning rate (0.05), depth (5), number of iterations (1000), and using GPU for speed enhancement were set.

- Training Results: 
     - The model achieved 92% accuracy on the training data.
     - The accuracy on the test data was 85%.
   - Confusion Matrix: A confusion matrix was created to visualize the model's performance, showing how many true positives, true negatives, false positives, and false negatives were predicted.

2. Feature Importance: The feature importance plot was generated to understand which features were most influential in predicting the outcome of diabetes. Features such as Glucose, BMI, and Insulin were the most important in determining the outcome.

3. Ensemble Model:
   - An ensemble model combining Random Forest and CatBoost was used to improve predictive performance.
   - Training Results: 
     - On the training data, the ensemble model achieved 100% accuracy.
     - On the test data, the accuracy dropped slightly to 84%.
   - Cross-validation: When cross-validation was applied, the ensemble model achieved an average accuracy of 81%, which helped to validate the model's robustness.
   
4. Sequence Model: A Sequential model was also trained, and it achieved an accuracy of 84% on the test data, showing that different algorithms could perform similarly on this task.

6) ## Final Evaluation and Results:

- The final ensemble model, which combined Random Forest and CatBoost, performed best on the training data with 100% accuracy, but slightly less on the test data (84% accuracy).
- Cross-validation results: On cross-validation, the model achieved an accuracy of 81%.
- Precision, Recall, and F1-Score: Precision, recall, and F1-score were calculated to assess the model's performance on both classes (diabetic vs non-diabetic). The performance on the test set was good, with reasonable values for precision, recall, and F1-score.

7) ## Conclusion:

This project demonstrates how machine learning algorithms such as CatBoost, Random Forest, and ensemble methods can be applied to predict diabetes based on medical features. The models performed well in predicting the presence of diabetes, and the use of techniques like SMOTETomek, MinMaxScaling, and LOF improved the overall performance of the models. The final ensemble model provided robust results, making it suitable for real-world applications in healthcare for early detection of diabetes.
