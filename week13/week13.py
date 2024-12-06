# from flask import Flask, request, render_template
# import sqlite3

# app = Flask(__name__, static_folder="static")

# @app.route('/', methods = ['GET', 'POST'])
# def home():
#     if request.method == 'POST':
#         fname = request.form.get('fname')
#         lname = request.form.get('lname')
#         feedback = request.form.get('feedback')
#         return render_template('formcomplete.html', fname=fname, lname=lname, feedback=feedback)
#     return render_template('form.html')

# if __name__ == "__main__":
#     app.run(debug = True)

# connection = sqlite3.connect("week13/static/feedbackdatabase.db")
# cursor = connection.cursor()
# # cursor.execute('''
# # CREATE TABLE IF NOT EXISTS userslist (
# # id INTEGER PRIMARY KEY,
# # fname TEXT,
# # lname TEXT
# # )''')
# # cursor.execute("INSERT INTO userslist (id,fname,lname) VALUES (?,?,?)", (1, "Alex", "Caraway"))
# # cursor.execute("INSERT INTO userslist (id,fname,lname) VALUES (?,?,?)", (2, "Nick", "Caraway"))
# # cursor.execute("INSERT INTO userslist (id,fname,lname) VALUES (?,?,?)", (3, "Maxwell", "Advancing-Technology"))
# # connection.commit()
# # connection.close()

# cursor.execute("SELECT * FROM userslist")
# rows = cursor.fetchall()

# for row in rows:
#     print(row)

# connection.close()

from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_folder="static")

def initDatabase():
    connection = sqlite3.connect("week13/static/feedbackdatabase.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS feedbacktable (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                   fname TEXT NOT NULL,
                   lname TEXT NOT NULL,
                   feedback TEXT NOT NULL)
                ''')
    connection.commit()
    connection.close()

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        feedback = request.form.get('feedback')
        connection = sqlite3.connect("week13/static/feedbackdatabase.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO feedbacktable (fname,lname,feedback) VALUES (?,?,?)", fname, lname, feedback)
        connection.commit()
        connection.close()
        return render_template('formcomplete.html', fname=fname, lname=lname, feedback=feedback)
    return render_template('form.html')

if __name__ == "__main__":
    initDatabase()
    app.run(debug = True)