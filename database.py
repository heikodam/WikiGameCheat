import mysql.connector
from web_scraper import *

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "HDamaske",
    database = "wiki_sample"
)

my_cursor = mydb.cursor()


ll, dll = getAllUrl("/wiki/Germany")



#my_cursor.execute("CREATE DATABASE testdb")

# my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     print(db)

#my_cursor.execute("CREATE TABLE users (name VARCHAR(255), email VARCHAR(255), age INTEGER(3), user_id INTEGER AUTO_INCREMENT PRIMARY KEY)")

# my_cursor.execute("SHOW TABLES")
# for table in my_cursor:
#     print(table)

# sqlStuff = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
# record1 = ("John", "email@code.com", 46)

# my_cursor.execute(sqlStuff, record1)
# mydb.commit()