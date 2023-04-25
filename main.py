import streamlit as st 
from eda_app import run_eda_app
from ml_app import run_ml_app

def main():
    # Set page title and icon
    st.set_page_config(page_title="Bank Churn Prediction App", page_icon=":money_with_wings:")

    # Define page header
    st.title("Bank Churn Prediction Data App")
    st.subheader("Using Machine Learning to Detect Customers at Risk of Churn")

    # Define sidebar menu options
    menu = ["Home", "Exploratory Data Analysis", "Machine Learning", "About"]
    choice = st.sidebar.radio("Select a section:", menu)

    # Render selected page content
    if choice == "Home":
        st.markdown("### Welcome to the Bank Churn Prediction Data App!")
        st.write("This app helps businesses detect customers who are at risk of churning, which can help reduce customer attrition and increase revenue.")
        st.write("You can explore the app by selecting one of the options from the sidebar menu.")

    elif choice == "Exploratory Data Analysis":
        st.markdown("## Exploratory Data Analysis")
        st.write("This section provides a detailed analysis of the dataset used in the app.")
        run_eda_app()

    elif choice == "Machine Learning":
        st.markdown("## Machine Learning Predictor App")
        st.write("This section provides a machine learning-based solution to predict customer churn.")
        run_ml_app()

    else:
        st.markdown("## About the Author")
        st.write("Elvis K. Kipleting is a contemplative coder and analyst, specializing in data science and machine learning.")
        st.write("Contact email: elviskoech95@gmail.com")

if __name__ == '__main__':
    main()
