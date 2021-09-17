from bs4 import BeautifulSoup
import requests
import mysql.connector

# get car's name
car_name = input("please enter name of car that you want to know it's characteristics?\n")
car_name = car_name.lower()
# connect to the database
cnx = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'python_project')
cursor = cnx.cursor()

# # create database for first time
# cursor.execute("CREATE DATABASE python_project")

# # create table for first time
# cursor.execute("CREATE TABLE car (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), functionality VARCHAR(50), city VARCHAR(250), price VARCHAR(250), accident VARCHAR(250), year INT)")

c = 1
while c < 5 :
    # connect to the website
    url  = "https://www.truecar.com/used-cars-for-sale/listings/"+car_name+"/?page="+str(c)
    res  = requests.get(url)
    soup = BeautifulSoup(res.text, 'html5lib')

    # find product years of cars
    years = soup.find_all('span', class_ = 'vehicle-card-year font-size-1')
    # find prices of cars
    prices = soup.find_all('div', class_ = 'heading-3 margin-y-1 font-weight-bold')
    # find functionalities of cars
    functionalities = soup.find_all('div', class_ = 'd-flex w-100 justify-content-between')
    # find names of cars
    names = soup.find_all('span', class_ = 'vehicle-header-make-model text-truncate')
    # find cities of cars
    cities = soup.find_all('div', class_ = 'vehicle-card-location font-size-1 margin-top-1')
    # find status of accident
    accidents = soup.find_all('div', class_ = 'vehicle-card-location font-size-1 margin-top-1')
    c += 1
