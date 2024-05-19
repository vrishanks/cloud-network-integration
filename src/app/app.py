from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db')
def db_test():
    conn = mysql.connector.connect(
        host="<AWS_RDS_ENDPOINT>",
        user="<DB_USERNAME>",
        password="<DB_PASSWORD>",
        database="<DB_NAME>"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT DATABASE();")
    db_name = cursor.fetchone()
    cursor.close()
    conn.close()
    return f"Connected to database: {db_name}"

if __name__ == '__main__':
    app.run()
