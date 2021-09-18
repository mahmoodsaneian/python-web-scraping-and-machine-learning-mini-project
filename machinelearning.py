from sklearn import tree
import mysql.connector

x = []
y = []

# connect to the database
cnx = mysql.connector.connect(user = 'root', password = '13812002m', database = 'python_project', host = '127.0.0.1')
cursor = cnx.cursor()
# read from database
cursor.execute('SELECT name ,functionality, accident, year, price FROM car')
res = cursor.fetchall()


# get information of new car that we want to calculate it's price
name = input("please enter name of car :    ")
functionality = input("please enter functionality of car :    ")
accident = input("Did you accident with this car?YES or NO :    ")
if accident == 'NO' :
    accident = 1
else:
    accident = -1
year = input("please enter product's year of car :    ")


for i in range(0, len(res)) :
    tmp = list(res[i])
    if name.lower() == tmp[0].lower() :
        # functionality of car
        f = tmp[1].split(" ")
        f = f[0].replace(',', '.')
        # status of accident
        acc = 0
        if tmp[2] == 'NO':
            acc = 1
        else:
            acc = -1
        # price of car
        p = str(tmp[4]).lstrip("$").replace(',', '.')

        x.append([f, acc, tmp[3]])
        y.append(p)

# give data to machine
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

new_car = [[functionality,accident,year]]
answer = clf.predict(new_car)
print(answer)
