import random
import sqlite3
import flask
from flask import Flask, render_template, request, send_from_directory, jsonify
import requests
import os
import json

app = flask.Flask(__name__)

with open('config.json', 'r') as file:
    config = json.load(file)

conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        rsa_key TEXT,
        icon TEXT,
        time INTEGER
    )
''')
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS messages (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT,
#         rsa_key TEXT,
#         icon TEXT,
#         time INTEGER
#     )
# ''')
conn.commit()
conn.close()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/static/<filename>')
def send_static(filename):
    return send_from_directory('static', f"{filename}")

@app.route('/example_json', methods=['GET', 'POST'])
def login():
    data = {
        'name': 'Alice',
        'age': 30,
        'city': 'Wonderland'
    }
    return jsonify(data)

@app.route("/server-config")
def server_config():
    with open('config.json', 'r') as file:
        return file
    

@app.route("/browsing")
def browsing():
    return "Hello world!"

@app.route("/browsing/<path:path>")
def browsing2(path):
    return path

if __name__ == '__main__':
    app.run(host=config["flask-settings"]["ip"], port=config["flask-settings"]["port"], debug=config["flask-settings"]["debug"])
