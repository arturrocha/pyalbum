import os
from flask import Flask, render_template, url_for
app = Flask(__name__)


@app.route('/')
def home():
    path = 'static/pictures/'
    years = os.listdir(path)
    years.sort()
    return render_template('home.html', years=years)


@app.route('/year/<year>')
def show_months(year):
    path = f'static/pictures/{year}/'
    my_filter = ['.DS_Store']
    months = [month for month in os.listdir(path) if month not in my_filter]
    months.sort()
    return render_template('year.html', months=months, year=year)


@app.route('/pics/<period>')
def show_pics(period):
    year = period.split('_')[0]
    month = period.split('_')[1]
    page = int(period.split('_')[2])
    path = f'static/pictures/{year}/{month}/'
    pics = os.listdir(path)
    path = f'pictures/{year}/{month}/'
    my_filter = ['.DS_Store', '.mov', '.MOV']
    end = (page * 20) -1
    start = end - 19
    pics = [path + pic for pic in pics
            if not any(pic.endswith(f) for f in my_filter)]
    size = len(pics)
    if end > size:
        pics = pics[start:]
        next_page = False
    else:
        pics = pics[start:end]
        next_page = True
    return render_template('pics.html', pics=pics, page=page, next_page=next_page, year=year, month=month)
