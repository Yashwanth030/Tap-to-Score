# Tap to Score – Flask Web App
A simple web-based game where users tap a button to increase their score and submit it to a MySQL database. Built using Flask for the backend and vanilla JavaScript for the frontend.

## Project Structure
tap_to_score/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css 
├── README.md

 ## Features
- Tap-based scoring system

- Scores stored in a MySQL database

- API to fetch all scores

## Setup Instructions

1. Clone the Repository
cd tap-to-score

3. Install Python Packages
Make sure you have Flask and MySQL connector installed:

pip install flask mysql-connector-python

3. Configure the MySQL Database
Run this SQL in your MySQL client:

CREATE DATABASE IF NOT EXISTS game_scores;

USE game_scores;

CREATE TABLE IF NOT EXISTS scores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    score INT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
Update the db_config in app.py with your MySQL credentials:

db_config = {
    'user': 'root',
    'password': 'YOUR_PASSWORD',
    'host': 'localhost',
    'database': 'game_scores'
}

4. Run the Flask App
python app.py


