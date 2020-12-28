import os
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    path = 'static/pictures/'
    years = os.listdir(path)
    pics = ['/pictures/2013/06/DDXN8527.jpeg']
    return render_template('home.html', pics=pics, years=years)


@app.route('/year/<year>')
def show_months(year):
    path = f'static/pictures/{year}/'
    my_filter = ['.DS_Store']
    months = [month for month in os.listdir(path)  if month not in my_filter]
    return render_template('year.html', months=months, year=year)


@app.route('/pics/<period>')
def show_pics(period):
    year = period.split('_')[0]
    month = period.split('_')[1]
    path = f'static/pictures/{year}/{month}/'
    pics = os.listdir(path)
    path = f'pictures/{year}/{month}/'
    pics = [path + pic for pic in pics]
    return render_template('pics.html', pics=pics)
