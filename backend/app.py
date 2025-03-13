import os
import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

# Database connection
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_NAME = os.getenv('DB_NAME', 'mydatabase')
DB_USER = os.getenv('DB_USER', 'myuser')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'mypassword')

try:
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print("✅ Successfully connected to PostgreSQL!")
except Exception as e:
    print(f"❌ Database connection error: {e}")

@app.route('/')
def home():
    return jsonify({"message": "Connected to PostgreSQL!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
