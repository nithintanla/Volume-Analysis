import streamlit as st
import pandas as pd
from connection import Client
from queries import get_queries
from styles import dashboard_css
from components import display_widget

# Streamlit app
st.set_page_config(layout="wide")
st.title("ClickHouse Dashboard")

# Date filters
start_date = st.date_input("Select start date", pd.to_datetime("today"))
end_date = st.date_input("Select end date", pd.to_datetime("today"))

# Apply custom CSS
st.markdown(dashboard_css, unsafe_allow_html=True)

# Get queries
queries = get_queries(start_date, end_date)

# Execute the queries and fetch the results into DataFrames
total_user_base_df = Client.query_df(queries['total_user_base'])
otp_user_base_df = Client.query_df(queries['otp_user_base'])
promotional_user_base_df = Client.query_df(queries['promotional_user_base'])
transactional_user_base_df = Client.query_df(queries['transactional_user_base'])
weekly_user_base_df = Client.query_df(queries['weekly_user_base'])

# Create columns for layout
col1, col2 = st.columns(2)

# Display the results as dashboard widgets with graphs
display_widget("Total User Base", total_user_base_df['total_user_base'][0], weekly_user_base_df, col1, 'blue')
display_widget("OTP User Base", otp_user_base_df['otp_user_base'][0], weekly_user_base_df, col2, 'green')
display_widget("Promotional User Base", promotional_user_base_df['promotional_user_base'][0], weekly_user_base_df, col1, 'red')
display_widget("Transactional User Base", transactional_user_base_df['transactional_user_base'][0], weekly_user_base_df, col2, 'purple')