import streamlit as st
import plotly.express as px

def display_widget(title, value, weekly_data, col, color):
    # Ensure the DataFrame has the correct columns
    if 'week_start' not in weekly_data.columns or 'week_end' not in weekly_data.columns or 'user_base' not in weekly_data.columns:
        st.error(f"Data for {title} is not available.")
        return
    
    # Create a new column for the week range
    weekly_data['week_range'] = weekly_data.apply(lambda row: f"{row['week_start'].strftime('%b %d')}-{row['week_end'].strftime('%b %d')}", axis=1)
    
    formatted_value = f"{value:,}"  # Format the value with thousand separators
    fig = px.bar(weekly_data, x='week_range', y='user_base', title=f"{title} Weekly Growth", color_discrete_sequence=[color])
    fig.update_layout(margin=dict(l=0, r=0, t=30, b=0), height=250)  # Increase the height of the graph
    
    col.markdown(f"""
        <div class="dashboard-widget">
            <p>{title}</p>
            <h2>{formatted_value}</h2>
            <div class="graph">
                <!-- Placeholder for the graph -->
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Render the graph separately
    with col:
        st.plotly_chart(fig, use_container_width=True)