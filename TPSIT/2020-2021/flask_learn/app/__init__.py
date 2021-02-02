from flask import Flask,session

app = Flask(__name__)


app.secret_key = "xxxx"

from app import routes