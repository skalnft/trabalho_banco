# import pyodbc
import pymssql

server = 'LENOVO-MARVIN'
database = 'PAISES'
username = 'sa'
password = 'admin12345678.'


connec = pymssql.connect(server=server, database=database, user=username, password=password, port=1433)
cursor = connec.cursor()
