from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Configure MySQL database
app.config['MYSQL_HOST'] = 'database-1.cz9tcdurbrql.us-east-1.rds.amazonaws.com'
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'Clarusway_1'
app.config['MYSQL_DB'] = 'clarusway'
app.config['MYSQL_PORT'] = 3306

# Function to get a database connection
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB'],
            port=app.config['MYSQL_PORT']
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

# Create users table and populate with sample data (Run this code only once)
def initialize_db():
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        drop_table = 'DROP TABLE IF EXISTS users;'
        users_table = """
        CREATE TABLE users (
          username varchar(50) NOT NULL,
          email varchar(50),
          PRIMARY KEY (username)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
        """
        data = """
        INSERT INTO users 
        VALUES 
            ("Tuba", "tuba@amazon.com"),
            ("Ethan", "ethan@micrasoft.com"),
            ("mostafa", "mostafa@facebook.com"),
            ("sait", "sait@tesla.com"),
            ("busra","busra@google");
        """
        cursor.execute(drop_table)
        cursor.execute(users_table)
        cursor.execute(data)
        connection.commit()
        cursor.close()
        connection.close()

# Call initialize_db() only once to set up the database
# initialize_db()

# Find emails by keyword
def find_emails(keyword):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = f"SELECT * FROM users WHERE username LIKE %s;"
        cursor.execute(query, (f'%{keyword}%',))
        result = cursor.fetchall()
        user_emails = [(row[0], row[1]) for row in result]
        cursor.close()
        connection.close()
        if not user_emails:
            user_emails = [('Not found.', 'Not Found.')]
        return user_emails

# Insert a new email
def insert_email(name, email):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s;"
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        response = ''
        if len(name) == 0 or len(email) == 0:
            response = 'Username or email cannot be empty!!'
        elif not result:
            insert = "INSERT INTO users (username, email) VALUES (%s, %s);"
            cursor.execute(insert, (name, email))
            connection.commit()
            response = f'User {name} and {email} have been added successfully'
        else:
            response = f'User {name} already exists.'
        cursor.close()
        connection.close()
        return response

# Route for finding emails
@app.route('/', methods=['GET', 'POST'])
def emails():
    if request.method == 'POST':
        user_name = request.form['user_keyword']
        user_emails = find_emails(user_name)
        return render_template('emails.html', name_emails=user_emails, keyword=user_name, show_result=True)
    else:
        return render_template('emails.html', show_result=False)

# Route for adding new emails
@app.route('/add', methods=['GET', 'POST'])
def add_email():
    if request.method == 'POST':
        user_name = request.form['username']
        user_email = request.form['useremail']
        result = insert_email(user_name, user_email)
        return render_template('add-email.html', result_html=result, show_result=True)
    else:
        return render_template('add-email.html', show_result=False)

# Run the Flask application
if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port=80)
