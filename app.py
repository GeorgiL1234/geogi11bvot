# app.py
from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    conn = mysql.connector.connect(
        host=os.getenv('DB_HOST', 'db'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'password'),
        database=os.getenv('DB_NAME', 'mydatabase')
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from Database!'")
    message = cursor.fetchone()[0]
    conn.close()
    return f'Hello, World! {message}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
