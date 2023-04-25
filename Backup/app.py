import streamlit as st 
import streamlit.components.v1 as stc 
from eda_app import run_eda_app
from ml_app import run_ml_app


html_temp = """
		<div style="background-color:#204F52;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">Bank Churn Prediction Data App </h1>
		<h4 style="color:white;text-align:center;">Customer Churn </h4>
		<body style="background-color:#09814A;text-align:center;"></body>

		</div>
		"""
	
st.set_page_config(page_title="Bank Churn Prediction App")
def main():
	# st.title("ML Web App with Streamlit")
	stc.html(html_temp)

	menu = ["Home","EDA","ML","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		st.write("""
			### Detecting customers at risk of churn using Machine Learning
		
##### Customer retention is one of the primary growth pillars for products with a subscription-based business model. Several bad experiences – or even one – and a customer may quit. And if droves of unsatisfied customers churn at a clip, both material losses and damage to reputation would be enormous.
##### Customer churn (or customer attrition) is a tendency of customers to abandon a brand and stop being a paying client of a particular business.
##### Companies that constantly monitor how people engage with products, encourage clients to share opinions, and solve their issues promptly have greater opportunities to maintain mutually beneficial client relationships.
##### Many surveys focusing on customer acquisition and retention costs are available online. According to this one by Invesp, conversion rate optimization company, getting a new customer may cost up to five times more than retaining an existing customer.
##### Sales, customer success, and marketing teams can also use the knowledge from the data analysis to align their actions.
			#### Datasource
			    - https://github.com/ezgicn/Project_EDA/blob/master/Churn.csv
			#### App Content
				- EDA Section: Exploratory Data Analysis of Data
				- ML Section: ML Predictor App

			""")
	elif choice == "EDA":
		run_eda_app()
	elif choice == "ML":
		run_ml_app()
	else:
		st.subheader("About")
		st.text("Contemplative coder and analyst")
		st.text("elviskoech95@gmail.com")
		st.text("Yours truly,")
		st.text("Elvis K. Kipleting")
		

if __name__ == '__main__':
	main()