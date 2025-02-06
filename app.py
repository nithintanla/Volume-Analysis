import streamlit as st
import pandas as pd
from connection import create_client
from queries import get_queries
from styles import dashboard_css
from components import display_widget

# Streamlit app
st.set_page_config(layout="wide")
st.title("ClickHouse Dashboard")

# Date filters
start_date = st.date_input("Select start date", pd.to_datetime("today"))
end_date = st.date_input("Select end date", pd.to_datetime("today"))

# Msg Status filter
msg_status = st.selectbox("Select Msg Status", ["Submitted", "Google submitted", "Delivered", "Read"])

# Apply custom CSS
st.markdown(dashboard_css, unsafe_allow_html=True)

# Get queries
queries = get_queries(start_date, end_date, msg_status)

# Create separate client instances for each query
client1 = create_client()
client2 = create_client()
client3 = create_client()
client4 = create_client()
client5 = create_client()
client6 = create_client()
client7 = create_client()
client8 = create_client()

# Execute the queries and fetch the results into DataFrames
total_volume_df = client1.query_df(queries['total_volume'])
otp_volume_df = client2.query_df(queries['otp_volume'])
promotional_volume_df = client3.query_df(queries['promotional_volume'])
transactional_volume_df = client4.query_df(queries['transactional_volume'])
weekly_total_volume_df = client5.query_df(queries['weekly_total_volume'])
weekly_otp_volume_df = client6.query_df(queries['weekly_otp_volume'])
weekly_promotional_volume_df = client7.query_df(queries['weekly_promotional_volume'])
weekly_transactional_volume_df = client8.query_df(queries['weekly_transactional_volume'])

# Create columns for layout
col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

# Display the results as dashboard widgets
col1.metric("Total Volume", f"{total_volume_df['total_volume'][0]:,}")
col2.metric("OTP Volume", f"{otp_volume_df['otp_volume'][0]:,}")
col3.metric("Promotional Volume", f"{promotional_volume_df['promotional_volume'][0]:,}")
col4.metric("Transactional Volume", f"{transactional_volume_df['transactional_volume'][0]:,}")

# Create columns for graphs
graph_col1, graph_col2, graph_col3, graph_col4 = st.columns(4)

# Display the graphs
display_widget("Total Volume", total_volume_df['total_volume'][0], weekly_total_volume_df, graph_col1, 'blue', None)
display_widget("OTP Volume", otp_volume_df['otp_volume'][0], weekly_otp_volume_df, graph_col2, 'green', 1)
display_widget("Promotional Volume", promotional_volume_df['promotional_volume'][0], weekly_promotional_volume_df, graph_col3, 'orange', 3)
display_widget("Transactional Volume", transactional_volume_df['transactional_volume'][0], weekly_transactional_volume_df, graph_col4, 'purple', 2)