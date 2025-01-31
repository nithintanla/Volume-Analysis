def get_queries(start_date, end_date):
    return {
        'total_user_base': f"""
            SELECT COUNT(*) as total_user_base
            FROM cdr_maap.mt_cdr_final
            WHERE dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
        """,
        'otp_user_base': f"""
            SELECT COUNT(*) as otp_user_base
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 1
        """,
        'promotional_user_base': f"""
            SELECT COUNT(*) as promotional_user_base
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 3
        """,
        'transactional_user_base': f"""
            SELECT COUNT(*) as transactional_user_base
            FROM cdr_maap.mt_cdr_final AS cdr
            JOIN cdr_maap.ENT_AGENTS AS agents ON cdr.vcAgentID = agents.vcAgentID
            WHERE cdr.dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            AND agents.iTrafficType = 2
        """,
        'weekly_user_base': f"""
            SELECT 
                toStartOfInterval(dtEntSubmit, INTERVAL 1 WEEK) as week_start, 
                toStartOfInterval(dtEntSubmit, INTERVAL 1 WEEK) + INTERVAL 6 DAY as week_end,
                COUNT(*) as user_base
            FROM cdr_maap.mt_cdr_final
            WHERE dtEntSubmit BETWEEN '{start_date}' AND '{end_date}'
            GROUP BY week_start, week_end
            ORDER BY week_start
        """
    }