from fastapi import FastAPI
import sqlite3

app = FastAPI()

app.get("/get_arabic_name")
def get_names():
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    cursor.execute("Select * FROM NAME")
    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        first_name = row[0]
        last_name = row[1]
        language = row[2]
        meaning = row[3]

        print(f"{first_name} {last_name} {language} {meaning}")