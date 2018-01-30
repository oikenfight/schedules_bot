from flask import request, redirect, url_for, render_template, flash, jsonify
from flaskr import app
from flaskr import config
from flaskr import calendars


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_schedules')
def get_schedules():
    start_date = request.args.get('name')
    finish_date = request.args.get('name')

    # 指定期間中のスケジュールを取得
    events = calendars.main()
    return jsonify(events)


@app.route('/get_free_schedules')
def get_free_schedules():
    start_date = request.args.get('name')
    finish_date = request.args.get('name')

    # 指定期間中のスケジュールを取得
    events = calendars.main()
    # TODO: 取得したスケジュールの中からスケジュールが入っていない日程を取り出す
    return jsonify


@app.route('/add', methods=['POST'])
def post():
    return redirect(url_for('index'))
