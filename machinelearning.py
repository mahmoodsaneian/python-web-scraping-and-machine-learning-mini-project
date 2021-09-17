from sklearn import tree
import mysql.connector

# connect to the database
cnx = mysql.connector.connect(user = 'root', password = '', database = 'python_project', host = '127.0.0.1')
cursor = cnx.cursor()
# read from database
cursor.execute('SELECT name, functionality, accident, year FROM car')
res = cursor.fetchall()

