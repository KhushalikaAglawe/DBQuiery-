# ROLE-2: SQL + Database
# Ensure read-only, no SELECT * (simple check)

def validate_sql(sql):
    try:
        if not sql.strip().lower().startswith("select"):
            return {"status": "error", "sql": None, "message": "Only SELECT queries allowed"}
        if "*" in sql:
            return {"status": "error", "sql": None, "message": "SELECT * not allowed"}
        return {"status": "ok", "sql": sql, "message": "SQL validated"}
    except Exception as e:
        return {"status": "error", "sql": None, "message": str(e)}
