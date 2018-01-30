from flask import request, redirect, url_for, render_template, flash, jsonify
from flaskr import app
from flaskr import calendars


@app.route('/')
def index():
    calendars.main()
    return render_template('index.html')


@app.route('/get_schedules')
def get_schedules():
    events = calendars.main()
    return jsonify(events)


@app.route('/add', methods=['POST'])
def post():
    return redirect(url_for('index'))
