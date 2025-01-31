import clickhouse_connect

# Define connection parameters
insight_host = '10.10.3.66'
username = 'nithindidigam'
password = '66zDxmXc'
port = 8123

# Function to create a new ClickHouse client
def create_client():
    return clickhouse_connect.get_client(
        host=insight_host,
        username=username,
        password=password,
        port=port
    )

# Create a ClickHouse client
client = create_client()

# Export the client as Client
Client = client