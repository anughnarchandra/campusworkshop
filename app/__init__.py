"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi83q3hp8u7g2ehbkmg-a",
        database="todo_dbh5",
        user="root",
        password="HAlYbRE3YEXERwQKAWkEMYasNP4foz90")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
