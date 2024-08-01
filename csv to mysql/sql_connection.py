import mysql.connector as msql
from mysql.connector import Error

def create_db():
    try:
        conn=msql.connect(host='localhost',user='root',password='1234')
        if conn.is_connected():
            cursor=conn.cursor()
            cursor.execute("create database csvdata")
            print("Database created")
    except Error as e:
        print("Error connecting DB",e)

def create_table(exceldata):
    try:
        conn=msql.connect(host='localhost',user='root',password='1234')
        if conn.is_connected():
            cursor=conn.cursor()
            cursor.execute("use csvdata")
            cursor.execute("select database();")
            record=cursor.fetchone()
            print("DB connected",record)
            cursor.execute("drop table if exists userdata;")
            print("DB Table creating..")
            cursor.execute("create table userdata(name varchar(15),age int,city varchar(30));")
            print("Table created..")
            for i,row in exceldata.iterrows():
                query="insert into csvdata.userdata values (%s,%s,%s)"
                cursor.execute(query,tuple(row))
            print("Record inserted")
            conn.commit()
    except Error as e:
        print("Error connected DB",e)

def select():
    try:
        conn = msql.connect(host='localhost', user='root', password='1234')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select * from csvdata.userdata;")
            result=cursor.fetchall()
            for i in result:
                print(i)
    except Error as e:
        print("Error connected DB",e)


