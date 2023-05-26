from flask import Flask, jsonify
import requests
import _mysql_connector

app = Flask(__name__)

def get_records_from_db():
    conn = _mysql_connector.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM table_name')
    records = cursor.fetchall()
    conn.close()
    return records

@app.route('/get_todos_from_db', methods=['GET'])
def get_todos_from_db():
    response = requests.get('http://localhost:5000/todos')
    todos = response.json()
    db_records = get_records_from_db()

    return jsonify({
        'todos': todos,
        'db_records': db_records
    }), 200

if __name__ == '__main__':
    app.run()
