from flask import Flask, request, redirect, render_template
import pymysql
import time

app = Flask(__name__)

def connect_with_retry():
    for i in range(10):  # retry up to 10 times
        try:
            db = pymysql.connect(
                host="db",          # MySQL service name
                user="notesuser",
                password="123456",
                database="notesdb"
            )
            print("✅ Connected to MySQL!")
            return db
        except pymysql.err.OperationalError as e:
            print(f"⏳ Attempt {i+1}/10: Database not ready ({e}), retrying in 3s...")
            time.sleep(3)
    raise Exception("❌ Could not connect to database after several attempts")

db = connect_with_retry()

@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = db.cursor()
    if request.method == 'POST':
        note = request.form['note']
        cursor.execute("INSERT INTO notes (content) VALUES (%s)", (note,))
        db.commit()
        return redirect('/')

    cursor.execute("SELECT content, created_at FROM notes ORDER BY created_at DESC")
    notes = cursor.fetchall()

    return render_template("index.html", notes=notes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

