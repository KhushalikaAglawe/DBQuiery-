# ROLE-2: SQL + Database
# Convert logical plan → MySQL SELECT query

def generate_sql(logical_plan):
    try:
        question = logical_plan.get("question", "").lower()
        
        # Starter patterns
        if "customer" in question:
            sql = "SELECT CustomerId, FirstName, LastName FROM Customer LIMIT 5;"
        elif "artist" in question:
            sql = "SELECT ArtistId, Name FROM Artist LIMIT 5;"
        elif "invoice" in question:
            sql = "SELECT InvoiceId, CustomerId, Total FROM Invoice LIMIT 5;"
        else:
            sql = "SELECT CustomerId, FirstName, LastName FROM Customer LIMIT 5;"
        
        return {"status": "ok", "sql": sql, "message": "SQL generated successfully"}
    
    except Exception as e:
        return {"status": "error", "sql": None, "message": str(e)}
