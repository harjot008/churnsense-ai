import streamlit as st
import pandas as pd

# Config the page
st.set_page_config(
    page_title="Telecom Churn Predictor",
    page_icon="📞"
)

# Title of the page
st.title("_Churn_ prediction app :sunglasses:", text_alignment='center')

# Divider after title
st.divider()

# Current given data to predict
st.subheader("Data given to predict", divider="yellow")

# Dummy DataFrame
pd = pd.DataFrame(
    [["No", "Yes", "Male", 1]], columns=["IsMarried", "Parent", "Gender", "haveJob"]
)

# Show the dummy DataFrame
st.dataframe(pd)

# Sidebar for input values to predict
st.sidebar.title("Input values")

    # These are the columns:
    # 'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    #    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    #    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
    #    'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
    #    'MonthlyCharges', 'TotalCharges'

    # "TotalCharges" - int64 - And if not available get that from total_charges of training set

    # flow of program:
    #     TotalCharges int -> handle every column like originally it was with same categories-> put the data to the pipeline

    # Assumptions:
    #     As an MVP we do not allow None values passed to a column

# Gender
gender = st.sidebar.selectbox(
    "Select gender",
    ["Male", "Female"]
)

st.write("Selected gender:", gender)

# Senior Citizen
senior_citizen = st.sidebar.selectbox(
    "Are you senior citizen?",
    ["Yes", "No"]
)

senior_citizen = 1 if senior_citizen == "Yes" else 0

# Partner
partner = st.sidebar.selectbox(
    "Do have have any partner?",
    ["Yes", "No"]
)

# Dependents column
dependents = st.sidebar.selectbox(
        "Do you have dependents?",
        ["No", "Yes"]
)

# tenure column
tenure = st.sidebar.slider(
        "Tenure in months",
        min_value=0,
        max_value=100,
        value=1,
        step=1
)

# PhoneService column
phone_service = st.sidebar.selectbox(
        "Phone service",
        ["No", "Yes"]
)

multiple_lines = st.sidebar.selectbox(
        "Multiple lines",
        ["No phone service", "No", "Yes"]
    )

internet_service = st.sidebar.selectbox(
        "Internet service",
        ["DSL", "Fiber optic", "No"]
    )

online_security = st.sidebar.selectbox(
    "Online security",
    ["No", "Yes", "No internet service"]
)

online_backup = st.sidebar.selectbox(
    "Online backup",
    ["Yes", "No", "No internet service"]
)

device_protection = st.sidebar.selectbox(
    "Device protection",
    ["No", "Yes", "No internet service"]
)

tech_support = st.sidebar.selectbox(
    "Tech support",
    ["No", "Yes", "No internet service"]
)

streaming_tv = st.sidebar.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

streaming_movies = st.sidebar.selectbox(
    "Streaming movies",
    ["No", "Yes", "No internet service"]
)

contract = st.sidebar.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

paperless_billing = st.sidebar.selectbox(
    "Paperless billing",
    ["Yes", "No"]
)

payment_method = st.sidebar.selectbox(
    "Payment method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

# monthly charges and total charges
monthly_charges = st.sidebar.number_input(
    "Monthly charges",
    min_value=0.0,
    max_value=150.0,
    value=20.0,
    step=0.1
)

total_charges = st.sidebar.number_input(
    "Total charges",
    min_value=0.0,
    max_value=10000.0,
    value=20.0,
    step=0.1
)
