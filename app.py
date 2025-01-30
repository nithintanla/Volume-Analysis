import streamlit as st
import pandas as pd
import clickhouse_connect

# Define connection parameters
insight_host = '10.10.3.66'
username = 'nithindidigam'
password = '66zDxmXc'
port = 8123

# Create a ClickHouse client
client = clickhouse_connect.get_client(
    host=insight_host,
    username=username,
    password=password,
    port=port
)

# Define the query
query = """
SELECT * FROM cdr_maap.mt_cdr_final LIMIT 10000
"""

# Execute the query and fetch the result into a DataFrame
df = client.query_df(query)

# Streamlit app
st.title("ClickHouse Dashboard")

# Display the dataframe
st.write(df)

# Create a bar chart (example)
st.bar_chart(df[['iGoogleSubmitStatus', 'iGoogleErrorCode']])