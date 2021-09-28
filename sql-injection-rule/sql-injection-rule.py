import re
from flask import app, request
import django.http
import sqlite3
import mysql.connector
import pymysql.cursors
import psycopg2
from sqlalchemy import create_engine


# sqlite3: + concatenation
def non_conformant_1(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# sqlite3: {} + .format concatenation
def non_conformant_2(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {};".format(name)
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# sqlite3: {id} + .format concatenation
def non_conformant_3(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {name1};".format(name1=name)
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# sqlite3: % concatenation
def non_conformant_4(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;" % (name)
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# sqlite3: concatenation AND params attribute of execute
def non_conformant_5(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> ?;"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    connection.close()


# sqlite3: executemany
def non_conformant_6(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> ?;"
    names_list = [('username',), (name,),('name',)]
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.executemany(query, names_list)
    connection.commit()
    connection.close()


# sqlite3: executescript
def non_conformant_7(request):
    name = request.GET.get("name")
    query = """
    SELECT *
    FROM Users
    WHERE name = {};

    SELECT *
    FROM Vehicles;
    """.format(name)
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()
    connection.close()


# mysql.connector: + concatenation
def non_conformant_8(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.close()
    connection.close()


# mysql.connector: {} + .format concatenation
def non_conformant_9(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {};".format(name)
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# mysql.connector: {id} + .format concatenation
def non_conformant_10(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {name1};".format(name1=name)
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# mysql.connector: % concatenation
def non_conformant_11(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;" % (name)
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# mysql.connector: concatenation AND params attribute of execute
def non_conformant_12(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> %s;"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    connection.close()


# mysql.connector: executemany
def non_conformant_13(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> %s;"
    names_list = [('username',), (name,),('name',)]
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.executemany(query, names_list)
    connection.commit()
    connection.close()


# psycopg2: + concatenation
def non_conformant_14(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2: {} + .format concatenation
def non_conformant_15(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {};".format(name)
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2: {id} + .format concatenation
def non_conformant_16(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {name1};".format(name1=name)
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2: % concatenation
def non_conformant_17(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;" % (name)
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2: concatenation AND params attribute of execute
def non_conformant_18(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> %s;"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    connection.close()


# psycopg2: executemany
def non_conformant_19(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> %s;"
    names_list = [('username',), (name,),('name',)]
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.executemany(query, names_list)
    connection.commit()
    connection.close()


# django: {} + .format concatenation
def non_conformant_20(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {};".format(name)
    cursor = connection.cursor()
    cursor.execute(query)


# django: {id} + .format concatenation
def non_conformant_21(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {name1};".format(name1=name)
    cursor = connection.cursor()
    cursor.execute(query)


# django: % concatenation
def non_conformant_22(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;" % (name)
    cursor = connection.cursor()
    cursor.execute(query)


# django: concatenation AND params attribute of execute
def non_conformant_23(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> %s;"
    cursor = connection.cursor()
    cursor.execute(query, [name])


# sqlalchemy: + concatenation
def non_conformant_24(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy: {} + .format concatenation
def non_conformant_25(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {};".format(name)
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy: {id} + .format concatenation
def non_conformant_26(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = {name1};".format(name1=name)
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy: % concatenation
def non_conformant_27(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;" % (name)
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy: concatenation AND params attribute of execute
def non_conformant_28(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name + " AND name <> %(name1)s;"
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query, {'name1':name})


# Flask web apps
@app.route('sqlInjection')
def non_conformant_29():
    name = request.args.get('name')
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


### Conformant ###


# sqlite3
def conformant_1(request):
    name = "Firstname Lastname"
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# sqlite3
def conformant_2(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name.strip('--') + ";"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# sqlite3
def conformant_3(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + re.sub('!@#$%^&*_-+=', '', name) + ";"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# sqlite3
def conformant_4(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = ?;"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    connection.close()


# sqlite3
def conformant_5(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = :name1;"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query, {"name1": name})
    connection.commit()
    connection.close()


# sqlite3
def conformant_6(request):
    name1 = "Firstname Lastname"
    name2 = "Lastname Firstname"
    query = "SELECT * FROM Users WHERE name = ?;"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.executemany(query, [(name1,),(name2,)])
    connection.commit()
    connection.close()


# sqlite3
def conformant_7(request):
    name = "Firstname Lastname"
    query = """
    SELECT *
    FROM Users
    WHERE name = {};

    SELECT *
    FROM Vehicles;
    """.format(name)
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()
    connection.close()


# sqlite3
def conformant_8(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + "Name" + ";"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# mysql.connector
def conformant_9(request):
    name = "Firstname Lastname"
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# mysql.connector
def conformant_10(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name.strip('--') + ";"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# mysql.connector
def conformant_11(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + re.sub('!@#$%^&*_-+=', '', name) + ";"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# mysql.connector
def conformant_12(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    connection.close()


# mysql.connector
def conformant_13(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %(name1)s;"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.execute(query, {"name1": name})
    connection.commit()
    connection.close()


# mysql.connector
def conformant_14(request):
    name1 = "Firstname Lastname"
    name2 = "Lastname Firstname"
    query = "SELECT * FROM Users WHERE name = %s;"
    connection = mysql.connector.connect(user='name')
    cursor = connection.cursor()
    cursor.executemany(query, [(name1,),(name2,)])
    connection.commit()
    connection.close()


# psycopg2
def conformant_15(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + "Name" + ";"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2
def conformant_16(request):
    name = "Firstname Lastname"
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2
def conformant_17(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name.strip('--') + ";"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2
def conformant_18(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + re.sub('!@#$%^&*_-+=', '', name) + ";"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# psycopg2
def conformant_19(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query, (name,))
    connection.commit()
    connection.close()


# psycopg2
def conformant_20(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %(name1)s;"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query, {"name1": name})
    connection.commit()
    connection.close()


# psycopg2
def conformant_21(request):
    name1 = "Firstname Lastname"
    name2 = "Lastname Firstname"
    query = "SELECT * FROM Users WHERE name = %s;"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.executemany(query, [(name1,),(name2,)])
    connection.commit()
    connection.close()


# psycopg2
def conformant_22(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + "Name" + ";"
    connection = psycopg2.connect("dbname=test user=postgres")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()


# django
def conformant_23(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + "Name" + ";"
    cursor = connection.cursor()
    cursor.execute(query)


# django
def conformant_24(request):
    from django.db import connection
    name = "Firstname Lastname"
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    cursor = connection.cursor()
    cursor.execute(query)


# django
def conformant_25(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name.strip('--') + ";"
    cursor = connection.cursor()
    cursor.execute(query)


# django
def conformant_26(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + re.sub('!@#$%^&*_-+=', '', name) + ";"
    cursor = connection.cursor()
    cursor.execute(query)


# django
def conformant_27(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %s;"
    cursor = connection.cursor()
    cursor.execute(query, [name])


# django
def conformant_28(request):
    from django.db import connection
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %(name1)s;"
    cursor = connection.cursor()
    cursor.execute(query, {"name1": name})



# sqlalchemy
def conformant_29(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + "Name" + ";"
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy
def conformant_30(request):
    name = "Firstname Lastname"
    query = "SELECT * FROM Users WHERE name = " + name + ";"
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy
def conformant_31(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + name.strip('--') + ";"
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy
def conformant_32(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = " + re.sub('!@#$%^&*_-+=', '', name) + ";"
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query)


# sqlalchemy
def conformant_33(request):
    name = request.GET.get("name")
    query = "SELECT * FROM Users WHERE name = %(name1)s;"
    engine = create_engine('sqlite:////tmp/test.db')
    connection = engine.connect()
    connection.execute(query, {"name1": name})


# Flask web app
@app.route('sqlInjection')
def conformant_34(request):
    name = request.args.get('name')
    query = "SELECT * FROM Users WHERE name = " + name.strip('--') + ";"
    connection = sqlite3.connect("amazon.db")
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    connection.close()

#################### interprocedural cases:
import sqlite3
from flask import request

def remove_email_from_all_subscriptions_return_count():
    db = sqlite3.connect("amazon.db")
    c = db.cursor()
    email = unsubscribe_all()
    c.execute("SELECT email FROM subscriptions WHERE email = %s" % email)

#URL handler to remove a user from all subscriptions
@app.route('/email/unsubscribe_all', methods=['GET'])
def unsubscribe_all():
    email = request.args.get('email')
    return email

def non_conformant_31(email):
    db = sqlite3.connect("amazon.db")
    c = db.cursor()
    c.execute("SELECT email FROM subscriptions WHERE email = %s" % email)

#URL handler to remove a user from all subscriptions
@app.route('/email/unsubscribe_all', methods=['GET'])
def user_input_email():
    email = request.args.get('email')
    non_conformant_31(email)

def removing_product():
    productId = request.args.get('productId')
    str = 'DELETE FROM products WHERE productID = ' + productId
    return str

def non_conformant_32():
    connection = psycopg2.connect("dbname=test user=postgres")
    cur = db.cursor()
    query = removing_product()
    cur.execute(query)

