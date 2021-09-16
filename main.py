import bs4
import requests
import mysql.connector

# get car's name
car_name = input("please enter name of car that you want to know it's characteristics?\n")

# connect to the database
cnx = mysql.connector.connect(user = 'root', password = '', host = '127.0.0.1', database = 'python_project')
cursor = cnx.cursor()

# # create database for first time
# cursor.execute("CREATE DATABASE python_project")

# # create table for first time
# cursor.execute("CREATE TABLE car (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), functionality VARCHAR(50), city VARCHAR(250), price VARCHAR(250), accident VARCHAR(250), year INT)")
