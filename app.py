from flask import Flask, render_template, request
import sqlite3




app = Flask(__name__)



@app.route("/")
def hello():
   return render_template("index.html")
@app.route("/get")
def hi():
   return render_template("sugget.html")
@app.route("/new")
def addnew():
   db = sqlite3.connect('data/database.db')
   cur = db.cursor()
   cur.execute("SELECT rowid, * FROM students")
   students = cur.fetchall()
   cur.close()
   db.close()
   return render_template('/student.html',students=students)

   
@app.route("/student", methods = ['POST', 'GET'])
def student():
   con = sqlite3.connect('data/database.db')
   cur = con.cursor()
   if request.method == 'POST':
         rowid = request.form['id']
         name = request.form['name']
         age = request.form['age']
         gen = request.form['gender']
         mar = request.form['major']
         if (request.form['actionadd'] == 'update'):
            try:
               # if request.form['actionadd'] == 'add':
               #    cur.execute("INSERT INTO students (name, age, gender, marjor) VALUES (?,?,?,?)",(name, age, gen, mar))
               # msg = "Record successfully added to database"
               cur.execute("UPDATE students SET name=?, age=?, gender=?, marjor=? WHERE rowid=?",(name, age, gen, mar, rowid))
               con.commit()

            except:
               con.rollback()
               msg = "Error in the INSERT"
            finally:
               # Send the transaction message to result.html
               cur.close()
         elif (request.form['actionadd'] == 'add'):
            try:
               cur.execute("INSERT INTO students (name, age, gender, marjor) VALUES (?,?,?,?)",(name, age, gen, mar))
               con.commit()
            except:
               con.rollback()
               msg = "Error in the INSERT"
            finally:
               # Send the transaction message to result.html
               cur.close()
         

   cur = con.cursor()
   cur.execute("SELECT rowid, * FROM students")
   students = cur.fetchall()
   cur.close()
   con.close()
   return render_template('/student.html',students=students)



@app.route("/dele", methods = ['POST', 'GET'])
def dele():
   con = sqlite3.connect('data/database.db')
   cur = con.cursor()
   if request.method == 'POST':
         rowid = request.form['id']
         try:
            
            cur.execute("DELETE FROM students WHERE rowid="+rowid)
            con.commit()
         except:
            con.rollback()
            msg = "Error in the INSERT"
         finally:
            # Send the transaction message to result.html
            cur.close()
      
   cur = con.cursor()
   cur.execute("SELECT rowid, * FROM students")
   students = cur.fetchall()
   cur.close()
   con.close()
   return render_template('/student.html',students=students)



if __name__ == "__main__": 
    app.run()