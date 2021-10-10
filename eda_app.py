from numpy import dtype
import streamlit as st 
import pandas as pd 

dataFrameSerialization = "legacy"

# Data Viz Pkgs
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 


@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df


def run_eda_app():
	st.subheader("EDA Section")
	df = load_data("data/bank_data_customer_churn.csv")
	df_clean = load_data("data/bank_data_customer_churn_clean.csv")
	

	submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		st.dataframe(df)
		
		with st.expander("Descriptive Summary"):
			st.dataframe(df_clean.describe())

		with st.expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())

		with st.expander("Target Distribution"):
			st.dataframe(df['Exited'].value_counts())
		with st.expander("Checking for Missing values"):
			st.dataframe(df.isnull().sum())
	
	
	else:
		st.subheader("Plots")
		# Layouts
		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Dist Plot of Gender"):

				#fig = plt.figure()
				#sns.countplot(df['Gender'])
				#st.pyplot(fig)

				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Gender Type','Counts']
				# st.dataframe(gen_df)
				p01 = px.pie(gen_df,names='Gender Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

		
		with col2:
			with st.expander("Dist Plot of Exited"):

				#fig = plt.figure()
				#sns.countplot(df['Gender'])
				#st.pyplot(fig)

				gen_df1 = df['Exited'].value_counts().to_frame()
				gen_df1 = gen_df1.reset_index()
				gen_df1.columns = ['Exited Type','Counts']
				# st.dataframe(gen_df)
				p02 = px.pie(gen_df1,names='Exited Type',values='Counts')
				st.plotly_chart(p02,use_container_width=True)

	


	    


		


	

		