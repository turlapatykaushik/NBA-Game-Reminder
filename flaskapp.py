# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:18:31 2022

@author: kturlapaty
"""

from flask import Flask, render_template, request
import urllib.request,json
from pymongo import MongoClient

#import psycopg2
from datetime import date

app = Flask(__name__)


client=MongoClient('localhost',27017)
db=client['nba']
collection=db['userDetails']


teamsList=['Atlanta Hawks', 'Boston Celtics', 'Brooklyn Nets',
           'Charlotte Hornets', 'Chicago Bulls', 'Cleveland Cavaliers',
           'Dallas Mavericks', 'Denver Nuggets', 'Detroit Pistons',
           'Golden State Warriors', 'Houston Rockets', 'Indiana Pacers',
           'Los Angeles Clippers', 'Los Angeles Lakers', 'Memphis Grizzlies',
           'Miami Heat', 'Milwaukee Bucks', 'Minnesota Timberwolves',
           'New Orleans Pelicans', 'New York Knicks', 'Oklahoma City Thunder',
           'Orlando Magic', 'Philadelphia 76ers', 'Phoenix Suns',
           'Portland Trail Blazers', 'Sacramento Kings','San Antonio Spurs',
           'Toronto Raptors', 'Utah Jazz', 'Washington Wizards']


@app.route('/')
def home():
    return render_template("index.html",listOfTeams=teamsList)



@app.route("/success" , methods=['GET', 'POST'])
def success():
    team = request.form.get("teamSelected")
    email = request.form.get("emailEntered")
    collection.insert_one({'team':team,'email':email})
    return('Success')
    #return(str(select1)+str(select2)+str(select3)) # just to see what select is

if __name__ == "__main__":
    app.run(debug=True)