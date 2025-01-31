dashboard_css = """
    <style>
    .dashboard-widget {
        background-color: #000000;
        color: #ffffff;
        padding: 10px; /* Reduce padding */
        border-radius: 10px;
        text-align: center;
        margin-bottom: 20px;
        height: 200px; /* Reduce the height of the card */
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 100%; /* Use the full width of the screen */
    }
    .dashboard-widget h2 {
        font-size: 1.5em; /* Reduce font size */
        margin: 0;
    }
    .dashboard-widget p {
        font-size: 1em; /* Reduce font size */
        margin: 0;
    }
    .dashboard-widget .graph {
        margin-top: 10px;
        height: 150px; /* Increase the height of the graph */
    }
    </style>
"""