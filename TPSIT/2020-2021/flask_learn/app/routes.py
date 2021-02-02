from os import error
from flask import render_template,request,redirect,session
from flask.helpers import url_for
#from werkzeug.wrappers import CommonRequestDescriptorsMixin
from app import app
import sqlite3
import hashlib
import re

regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

@app.route('/')
def Home():
   return redirect(url_for('Login'))


def validate(username,password):
   with sqlite3.connect('app/static/utents.db') as db:
      password = hashlib.sha224(bytes(password,encoding='utf-8')).hexdigest()
      c = db.cursor()
      c.execute('SELECT * FROM clienti  WHERE username = "%s" AND password ="%s"' % (username, password))
      if c.fetchone() is not None:
         return True
      else:
         return False

def registra(username,email,password):

         with sqlite3.connect('app/static/utents.db') as db:
            c = db.cursor()
            c.execute("INSERT INTO clienti (username,email,password) VALUES (?,?,?)",(username,email,password) )


@app.route('/regis', methods=['GET','POST'])
def Regis():
   errort = "Manca qualcosa ಠ╭╮ಠ "
   if request.method == 'POST':
      username = request.form['username']
      email = request.form['email']
      password = request.form['password']
      if username =="" and email =="" and password =="":
         return render_template("Login.html", erroregi = errort)
      if not(re.search(regex,email)):  
            errort = "Email non valida!ಠ╭╮ಠ'"
            return render_template("Login.html", erroregi = errort)
      if len(username)< 5:  
            errort = "Username troppo corto!ಠ╭╮ಠ'"
            return render_template("Login.html", erroregi = errort)
      if len(password)< 8:  
            errort = "Password troppo corta!(minimo 8 lettere)ಠ╭╮ಠ'"
            return render_template("Login.html", erroregi = errort)
      else:
         password = hashlib.sha224(bytes(password,encoding='utf-8')).hexdigest()
         registra(username,email,password)
         stri = "ti sei appena inscritto al sito! - \ (•◡•) /"
         return render_template("Login.html", regis = stri )


@app.route('/login', methods=['GET','POST'])
def Login():
   error = None
   if request.method == 'POST':
      print(request.form)
      username = request.form['username']
      password = request.form['password']
      completion = validate(username, password)
      if completion == False:
         error ='Non valido! ಠ╭╮ಠ'
      else:
         session['username'] = username
         return redirect(url_for('welcome',username=username))
   return render_template("Login.html", error = error)

@app.route('/welcome')
def welcome():
   username = request.args['username']
   username = session['username'] 
   return render_template('welcome.html',error= username)