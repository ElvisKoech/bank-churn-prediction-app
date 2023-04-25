import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Load data function
@st.cache_data
def load_data(data):
    df = pd.read_csv(data)
    return df


def run_eda_app():
    st.title("Exploratory Data Analysis")
    st.subheader("Bank Customer Churn Dataset")

    # Load the dataset
    df = load_data("data/bank_data_customer_churn.csv")

    # Sidebar menu for selection
    st.sidebar.title("Explore")
    menu = st.sidebar.radio("Select an option", ["Overview", "Descriptive", "Visualizations"])

    if menu == "Overview":
        st.write(
            """
            This is an exploratory data analysis application for a bank customer churn dataset. 
            You can use the sidebar to navigate through the different sections of this application. 
            """
        )

    elif menu == "Descriptive":
        # Display the dataset
        st.subheader("Descriptive Summary")
        st.dataframe(df.describe())

        # Display gender distribution
        st.subheader("Gender Distribution")
        gender_df = df["Gender"].value_counts().reset_index()
        gender_df.columns = ["Gender", "Count"]
        st.dataframe(gender_df)

        # Display target distribution
        st.subheader("Target Distribution")
        target_df = df["Exited"].value_counts().reset_index()
        target_df.columns = ["Exited", "Count"]
        st.dataframe(target_df)

        # Check for missing values
        st.subheader("Missing Values")
        missing_df = df.isnull().sum().reset_index()
        missing_df.columns = ["Feature", "Missing Count"]
        st.dataframe(missing_df)

    else:
        # Plot gender distribution
        st.subheader("Gender Distribution")
        gender_df = df["Gender"].value_counts().reset_index()
        gender_df.columns = ["Gender", "Count"]
        fig1 = px.pie(gender_df, names="Gender", values="Count", color="Gender", hole=0.6)
        st.plotly_chart(fig1, use_container_width=True)

        # Plot target distribution
        st.subheader("Target Distribution")
        target_df = df["Exited"].value_counts().reset_index()
        target_df.columns = ["Exited", "Count"]
        fig2 = px.pie(target_df, names="Exited", values="Count", color="Exited", hole=0.6)
        st.plotly_chart(fig2, use_container_width=True)

        # Display Correlation Heatmap
        st.subheader("Correlation Matrix")
        fig3 = px.imshow(df.corr(numeric_only=True))
        fig3.update_layout(
            title={
                "text": "Correlation Heatmap",
                "xanchor": "center",
                "yanchor": "top",
                "x": 0.5,
            },
            xaxis={"title": "Features"},
            yaxis={"title": "Features"},
        )
        st.plotly_chart(fig3, use_container_width=True)

        # Display Pairplot
        st.subheader("Pairplot")
        fig4 = px.scatter_matrix(
            df,
            dimensions=df.columns[:-1],
            color="Exited",
            symbol="Gender",
            title="Pairplot",
        )
        fig4.update_layout(height=700, width=700)
        st.plotly_chart(fig4, use_container_width=True)



		


	

		