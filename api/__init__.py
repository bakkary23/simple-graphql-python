from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ivbmuznv:fffoU4c8GpohljbUeu7PiFsfY450WY6N@kashin.db.elephantsql.com/ivbmuznv"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'THE TRACTOR STORY'