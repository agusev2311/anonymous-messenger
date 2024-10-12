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
print(config)

conn = sqlite3.connect('data.sqlite')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS requests (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        messages TEXT,
        response TEXT,
        user_id TEXT,
        time TEXT
    )
''')
conn.commit()
conn.close()

@app.route('/')
def favicon():
    return send_from_directory('../static', 'index.html')

@app.route('/static/<filename>')
def send_static(filename):
    return send_from_directory('../static', f"{filename}")

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
    return jsonify(config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
