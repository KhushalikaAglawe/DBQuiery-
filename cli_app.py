# ui/cli_app.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reasoning.reasoning_engine import get_reasoning
from sql_engine.sql_generator import generate_sql
from sql_engine.sql_validator import validate_sql
from sql_engine.sql_executor import execute_sql
from database.mysql_connector import get_connection

def display_cli(question, reasoning, sql, result, answer):
    print("\n" + "="*60)
    print(f"Question: {question}\n")
    
    print("Reasoning / Logical Plan:")
    for step in reasoning:
        print(f" - {step}")
    
    print(f"\nGenerated SQL:\n{sql}")
    print(f"\nQuery Result:\n{result}")
    print(f"\nAnswer:\n{answer}")
    print("="*60 + "\n")


def main():
    conn, cursor = get_connection()
    if not conn or not cursor:
        print("Cannot connect to MySQL. Check DB_CONFIG.")
        return

    # You can either read demo questions or ask live input
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ")
        if question.lower() in ["exit", "quit"]:
            break

        # Role-1: Reasoning
        reasoning_plan = {
            "question": question,
            "steps": [
                "Identify main entity and relevant table(s)",
                "Determine necessary columns",
                "Apply filters or aggregation if needed"
            ]
        }

        # Role-2: Generate SQL
        gen = generate_sql(reasoning_plan)
        if gen["status"] == "error":
            display_cli(question, reasoning_plan["steps"], None, None, f"SQL Generation Error: {gen['message']}")
            continue

        # Validate SQL
        val = validate_sql(gen["sql"])
        if val["status"] == "error":
            display_cli(question, reasoning_plan["steps"], gen["sql"], None, f"SQL Validation Error: {val['message']}")
            continue

        # Execute SQL
        exec_result = execute_sql(val["sql"], cursor)
        if exec_result["status"] == "error":
            display_cli(question, reasoning_plan["steps"], val["sql"], None, f"SQL Execution Error: {exec_result['message']}")
            continue

        # Display final results
        display_cli(question, reasoning_plan["steps"], val["sql"], exec_result["data"], f"Answer shown above")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
