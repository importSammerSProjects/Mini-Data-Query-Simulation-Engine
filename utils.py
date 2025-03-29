import re

# Simulates conversion from natural language to pseudo-SQL
def process_query(nl_query):
    query_mapping = {
        "show all users": "SELECT * FROM users;",
        "get orders from last month": "SELECT * FROM orders WHERE order_date > DATE_SUB(CURDATE(), INTERVAL 1 MONTH);",
        "total revenue": "SELECT SUM(amount) FROM transactions;"
    }
    return query_mapping.get(nl_query.lower(), "SELECT * FROM data WHERE condition;")

# Simulates query explanation
def explain_query(nl_query):
    explanations = {
        "show all users": "Fetching all users from the database.",
        "get orders from last month": "Retrieving all orders placed in the last 30 days.",
        "total revenue": "Calculating the total sum of all transactions."
    }
    return explanations.get(nl_query.lower(), "Query explanation is not available.")

# Validates if query is understandable
def validate_query(nl_query):
    known_queries = ["show all users", "get orders from last month", "total revenue"]
    return nl_query.lower() in known_queries
