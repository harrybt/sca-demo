from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Setup in-memory database
conn = sqlite3.connect(':memory:', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
cursor.execute("INSERT INTO users (username, password) VALUES ('admin', 'secret')")
conn.commit()

@app.route("/login", methods=["GET"])
def login():
    username = request.args.get("username", "")
    
    query = f"SELECT * FROM users WHERE username = '{username}'"
    result = cursor.execute(query).fetchall()

    if result:
        return f"Welcome {username}!"
    return "User not found", 404

if __name__ == "__main__":
    app.run(debug=True)
