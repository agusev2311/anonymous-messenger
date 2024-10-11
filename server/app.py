import random
import sqlite3
import flask
from flask import Flask, render_template, request, send_from_directory, jsonify
import requests
import os

app = flask.Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)