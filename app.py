from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'user': 'root',
    'password': 'Yashu@003',
    'host': 'localhost',
    'database': 'game_scores'
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_score', methods=['POST'])
def submit_score():
    score = request.json.get('score')
    if score is not None:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO scores (score) VALUES (%s)', (score,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Score submitted successfully!"}), 200
    else:
        return jsonify({"message": "Invalid score!"}), 400

@app.route('/get_scores')
def get_scores():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM scores')
    scores = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(scores), 200

if __name__ == '__main__':
    app.run(debug=True)
