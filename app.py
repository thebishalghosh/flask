from flask import Flask, render_template
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12784830',
    'password': 'sqCglBq6Xi',
    'database': 'sql12784830'
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/')
def index():
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            # Replace 'your_table' with your actual table name
            cursor.execute("SELECT * FROM student")
            data = cursor.fetchall()
            cursor.close()
            connection.close()
            return render_template('index.html', data=data)
        except Error as e:
            print(f"Error: {e}")
            return "Database error", 500
    return "Could not connect to database", 500

if __name__ == '__main__':
    app.run(debug=True)