from flask import Flask, request
from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost")
db = client['nba']

app = Flask(__name__)

@app.route('/predict/matchs/<homeTeam>/<awayTeam>')
def resultMatch(homeTeam, awayTeam):
    return json.dumps(resultMatch)

app.run("0.0.0.0", 5000, debug=True)