#!/usr/bin/env python
'''

All of the following exercises should be done using sqlalchemy.

Using the provided database schema, write the necessary code to print information about the film and category table.

'''
from pprint import pprint
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root@{password}localhost/sakila')

connection = engine.connect()
metadata = sqlalchemy.MetaData()

#Film data
film_table = sqlalchemy.Table('film', metadata, autoload=True, autoload_with=engine)

query = sqlalchemy.select([film_table])
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)

#category data
category_table = sqlalchemy.Table('category', metadata, autoload=True, autoload_with=engine)
query = sqlalchemy.select([category_table])
result_proxy = connection.execute(query)

result_set = result_proxy.fetchall()
pprint(result_set)
