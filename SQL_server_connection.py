# Importing Packages
import pyodbc 
import pandas as pd

server = 'server'
database = 'database'
username = 'username'
password = 'password'

# Establishing a connection to the SQL Server. Check ODBC Drivers for which version you have. Currently 11.
connection = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};\
                      SERVER='+server+';\
                      DATABASE='+database+';\
                      UID='+username+';\
                      PWD='+ password)

cursor = connection.cursor()

# Write the query here. Backslashes can be used to add new lines
query = "SELECT *\
            FROM table_name\
            WHERE column_name = '1234'"
                
# Converting the queried data to a pandas dataframe
df = pd.read_sql_query(query, connection)

# Printing the first 5 rows of the dataframe
print(df.head())
