from sklearn import tree
import mysql.connector

x = []
y = []

# connect to the database
cnx = mysql.connector.connect(user = 'root', password = '', database = 'python_project', host = '127.0.0.1')
cursor = cnx.cursor()
# read from database
cursor.execute('SELECT name, functionality, accident, year, price FROM car')
res = cursor.fetchall()

for i in range(0, len(res)) :
    tmp = list(res[i])
    x.append(tmp[0:4])
    y.append(tmp[4])

