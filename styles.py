dashboard_css = """
    <style>
    .dashboard-widget {
        background-color: #1f1f1f;
        color: #ffffff;
        padding: 15px; /* Adjust padding */
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        height: 250px; /* Adjust the height of the card */
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100%; /* Use the full width of the screen */
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Add shadow for depth */
    }
    .dashboard-widget h2 {
        font-size: 2em; /* Adjust font size */
        margin: 0;
        color: #ffcc00; /* Change color */
    }
    .dashboard-widget p {
        font-size: 1.2em; /* Adjust font size */
        margin: 0;
        color: #00ccff; /* Change color */
    }
    .dashboard-widget .graph {
        margin-top: 10px;
        height: 200px; /* Adjust the height of the graph */
    }
    </style>
"""