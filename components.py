import streamlit as st
import plotly.express as px

def display_widget(title, value, weekly_data, col, color, traffic_type):
    # Ensure the DataFrame has the correct columns
    if 'week_start' not in weekly_data.columns or 'week_end' not in weekly_data.columns or 'volume' not in weekly_data.columns:
        st.error(f"Data for {title} is not available.")
        return
    
    # Create a new column for the week range
    weekly_data['week_range'] = weekly_data.apply(lambda row: f"{row['week_start'].strftime('%b %d')}-{row['week_end'].strftime('%b %d')}", axis=1)
    
    formatted_value = f"{value:,}"  # Format the value with thousand separators
    fig = px.bar(weekly_data, x='week_range', y='volume', title=f"{title} Weekly Growth", color_discrete_sequence=[color])
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0), 
        height=250,  # Increase the height of the graph
        plot_bgcolor='#1f1f1f',  # Background color
        paper_bgcolor='#1f1f1f',  # Paper color
        font=dict(color='#ffffff'),  # Font color
        title_font=dict(size=20, color='#ffcc00', family="Arial"),  # Title font
        xaxis=dict(title='Week Range', tickangle=-45),  # X-axis title and angle
        yaxis=dict(title='Volume', tickformat=',d')  # Y-axis title and format
    )
    
    col.plotly_chart(fig, use_container_width=True)