# ROLE-1: Reasoning / Planner
# Generate a simple logical plan from user input

def get_reasoning():
    question = input("Enter your question: ")
    logical_plan = {
        "question": question,
        "type": "simple"  # placeholder, later can classify more
    }
    return logical_plan
