from fastapi import FastAPI
import sqlite3

app = FastAPI()

con=sqlite3.connect('spam.sqlite')
cursor = con.cursor()

@app.get("/all")
async def all_message():
    cursor.execute("""SELECT * FROM spam""")
    all = cursor.fetchall()
    return all

@app.get("/spam")
async def spam_message():
    cursor.execute("""SELECT * FROM spam
                   WHERE label='spam'""")
    spam = cursor.fetchall()
    return spam

@app.get("/ham")
async def ham_message():
    cursor.execute("""SELECT * FROM spam
                   WHERE label='ham'""")
    ham = cursor.fetchall()
    return ham
    