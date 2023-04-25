import streamlit as st 
import joblib
import os
import numpy as np


# Define label dictionaries and feature maps
label_dict = {"No": 0, "Yes": 1}
gender_map = {"Female": 0, "Male": 1}
target_label_map = {"No Churn": 0, "Churn": 1}
geography_label_map = {"France": 0, "Spain": 1, "Germany": 2}

# Define attribute information and instructions for input fields
attrib_info = """
#### Attribute Information:                    
 - CreditScore (range: 350-850)    
 - Geography          
 - Gender          
 - Age (range: 18-92)             
 - Tenure (range: 0-10)             
 - Balance (range: 0-300,000)            
 - NumOfProducts (range: 1-5)      
 - HasCrCard          
 - IsActiveMember   
 - EstimatedSalary (range: 10-200,000)
"""
instructions = {
    "CreditScore": "Enter your credit score (between 350 and 850).",
    "Geography": "Select the country where you live.",
    "Gender": "Select your gender.",
    "Age": "Enter your age (between 18 and 92).",
    "Tenure": "Enter the number of years you have been a customer (between 0 and 10).",
    "Balance": "Enter your bank balance (between 0 and 300,000).",
    "NumOfProducts": "Enter the number of bank products you have (between 1 and 5).",
    "HasCrCard": "Select whether you have a credit card or not.",
    "IsActiveMember": "Select whether you are an active member of the bank or not.",
    "EstimatedSalary": "Enter your estimated salary (between 10 and 200,000)."
}


@st.cache_resource
def load_model(model_file_lr):
    loaded_model = joblib.load(open(os.path.join(model_file_lr),"rb"))
    return loaded_model


# Define helper functions for encoding categorical values
def get_fvalue(val):
    feature_dict = {"No":0,"Yes":1}
    for key,value in feature_dict.items():
        if val == key:
            return value 

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value 

def run_ml_app():
	st.subheader("Machine Learning Section")
	
	loaded_model= load_model("models/logistic_Regression_model_customer_churn_2_oct_2021.pkl")
	with st.expander("Attributes Info"):
		st.markdown(attrib_info,unsafe_allow_html=True)


		CreditScore = st.number_input("CreditScore",350,900)
		Geography = st.selectbox("Geography",["France","Spain","Germany"])
		Gender = st.radio("Gender",["Female","Male"])
		Age = st.number_input("Age",15,100)
		Tenure = st.number_input("Tenure",0,10)
		Balance = st.number_input("Balance",0,300000)
		NumOfProducts = st.number_input("NumOfProducts",1,5)
		HasCrCard= st.radio("HasCrCard",["No","Yes"])
		IsActiveMember = st.radio("IsActiveMember",["No","Yes"])
		EstimatedSalary = st.number_input("EstimatedSalary",10,200000)


	with st.expander("Your Selected Options"):
		result={'CreditScore':CreditScore,
		'Geography':Geography,
		'Gender':Gender,
		'Age':Age,
		'Tenure':Tenure,
		'Balance':Balance,
		'NumOfProducts':NumOfProducts,
		'HasCrCard':HasCrCard,
		'IsActiveMember':IsActiveMember,
		'EstimatedSalary':EstimatedSalary}
		st.write(result)
		encoded_result = []
		for i in result.values():
			if type(i) == int:
				encoded_result.append(i)
			elif i in ["Female","Male"]:
				res = get_value(i,gender_map)
				encoded_result.append(res)
			elif i in ["France","Spain","Germany"]:
				res1 = get_value(i, geography_label_map)
				encoded_result.append(res1)
			else:
				encoded_result.append(get_fvalue(i))
		st.write(encoded_result)

	

	
	with st.expander("Prediction Results"):
		#single_sample = np.all(np.isfinite(encoded_result)).reshape(1,-1)
		single_sample = np.array(encoded_result).reshape(1,-1)

		
		prediction = loaded_model.predict(single_sample)
		pred_prob = loaded_model.predict_proba(single_sample)
		st.write(prediction)
		#st.write(pred_prob)


		if prediction == 1:
			st.warning("Churn-{}".format(prediction[0]))
			pred_probability_score = {"No Churn Probability Score":pred_prob[0][0]*100,"Churn Probability Score":pred_prob[0][1]*100}
			st.subheader("Prediction Probability Score")
			st.json(pred_probability_score)
		else:
			st.success("No Churn-{}".format(prediction[0]))
			pred_probability_score = {"No Churn Probability Score":pred_prob[0][0]*100,"Churn Probability Score":pred_prob[0][1]*100}
			st.subheader("Prediction Probability Score")
			st.json(pred_probability_score)
