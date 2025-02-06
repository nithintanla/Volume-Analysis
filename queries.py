def get_queries(start_date, end_date, msg_status):
    status_condition = ""
    if msg_status == "Google submitted":
        status_condition = "AND cdr.iGoogleSubmitStatus = 1"
    elif msg_status == "Delivered":
        status_condition = "AND cdr.iDRStatus = 1"
    elif msg_status == "Read":
        status_condition = "AND cdr.bIsRead = TRUE"

    return {
        'total_volume': f"""
            SELECT COUNT(*) as total_volume
            FROM cdr_maap.mt_cdr_final AS cdr
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            {status_condition}
        """,
        'otp_volume': f"""
            SELECT COUNT(*) as otp_volume
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 1
            {status_condition}
        """,
        'promotional_volume': f"""
            SELECT COUNT(*) as promotional_volume
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 3
            {status_condition}
        """,
        'transactional_volume': f"""
            SELECT COUNT(*) as transactional_volume
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 2
            {status_condition}
        """,
        'weekly_volume': f"""
            SELECT 
                toStartOfInterval(dtEntSubmit, INTERVAL 1 WEEK) as week_start, 
                toStartOfInterval(dtEntSubmit, INTERVAL 1 WEEK) + INTERVAL 6 DAY as week_end,
                agents.iTrafficType as traffic_type,
                COUNT(*) as volume
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            GROUP BY week_start, week_end, traffic_type
            ORDER BY week_start
        """,
        'weekly_total_volume': f"""
            SELECT 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) as week_start, 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) + INTERVAL 6 DAY as week_end,
                COUNT(*) as volume
            FROM cdr_maap.mt_cdr_final AS cdr
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            {status_condition}
            GROUP BY week_start, week_end
            ORDER BY week_start
        """,
        'weekly_otp_volume': f"""
            SELECT 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) as week_start, 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) + INTERVAL 6 DAY as week_end,
                COUNT(*) as volume
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 1
            {status_condition}
            GROUP BY week_start, week_end
            ORDER BY week_start
        """,
        'weekly_promotional_volume': f"""
            SELECT 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) as week_start, 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) + INTERVAL 6 DAY as week_end,
                COUNT(*) as volume
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 3
            {status_condition}
            GROUP BY week_start, week_end
            ORDER BY week_start
        """,
        'weekly_transactional_volume': f"""
            SELECT 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) as week_start, 
                toStartOfInterval(cdr.dtEntSubmit, INTERVAL 1 WEEK) + INTERVAL 6 DAY as week_end,
                COUNT(*) as volume
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 2
            {status_condition}
            GROUP BY week_start, week_end
            ORDER BY week_start
        """
    }