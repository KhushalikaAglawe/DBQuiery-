# ROLE-2: SQL + Database
# Execute SQL and handle errors

def execute_sql(sql, cursor):
    try:
        cursor.execute(sql)
        rows = cursor.fetchall()
        return {"status": "ok", "data": rows, "message": "Query executed successfully"}
    except Exception as e:
        return {"status": "error", "data": None, "message": str(e)}
