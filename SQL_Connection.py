import pyodbc


conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server= AYUSHP-DELL\\SQLEXPRESS03;'
                      'Database = TAPR102_1;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()





