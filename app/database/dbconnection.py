import pyodbc


connec = pyodbc.connect(
    "Driver={SQLDriverConnect};"
    "Server='';"
    "Database='';"
    "UID=user;"
    "PWD=password"
)

