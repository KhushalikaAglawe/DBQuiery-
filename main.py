from reasoning.reasoning_engine import get_reasoning
from sql_engine.sql_generator import generate_sql
from sql_engine.sql_validator import validate_sql
from sql_engine.sql_executor import execute_sql
from database.mysql_connector import get_connection
from ui.cli_app import display_result

def main():
    plan = get_reasoning()
    conn, cursor = get_connection()
    if not conn or not cursor:
        print("Cannot connect to MySQL. Check DB_CONFIG.")
        return

    gen = generate_sql(plan)
    if gen["status"] == "error":
        print("SQL Generation Error:", gen["message"])
        return

    val = validate_sql(gen["sql"])
    if val["status"] == "error":
        print("SQL Validation Error:", val["message"])
        return

    exec_result = execute_sql(val["sql"], cursor)
    if exec_result["status"] == "error":
        print("SQL Execution Error:", exec_result["message"])
        return

    display_result(plan, val["sql"], exec_result["data"])
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
