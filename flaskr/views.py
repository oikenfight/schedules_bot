from flask import request, redirect, url_for, render_template, flash, jsonify
from flaskr import app
from flaskr import config
from flaskr import calendars

import datetime
from pytz import timezone


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_schedules')
def get_schedules():
    """
    パラメータから日付を受け取り、その期間中のスケジュールを json で返却する
    :return json:
    """
    # パラメータを取得
    time_min = request.args.get('time_min')
    time_max = request.args.get('time_max')

    # UTC タイムゾーンに変換
    if time_min and time_max:
        time_min = datetime.datetime.strptime(time_min, '%Y-%m-%d')
        time_max = datetime.datetime.strptime(time_max, '%Y-%m-%d')
        # TODO: この方法で utc timezone に変換すると "+00:00" が末尾に付いて、期待するパラメータと形式が異なるため無理やり矯正
        time_min = timezone('UTC').localize(time_min).isoformat()[:-6] + 'Z'  # 'Z' indicates UTC time
        time_max = timezone('UTC').localize(time_max).isoformat()[:-6] + 'Z'  # 'Z' indicates UTC time
    else:
        time_min = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # TASK: 一週間後とかにしたいけど、日付関連だるいから後回し
        time_max = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    # 指定期間中のスケジュールを取得
    events = calendars.main(time_min, time_max)
    return jsonify(events)


@app.route('/get_free_schedules')
def get_free_schedules():
    """
    パラメータから日付を受け取り、その期間中のスケジュールを json で返却する
    :return json:
    """
    # パラメータから日付を取得
    date_min = request.args.get('time_min')
    date_max = request.args.get('time_max')

    between_days = 0

    # UTC タイムゾーンに変換
    if date_min and date_max:
        date_min = datetime.datetime.strptime(date_min, '%Y-%m-%d')
        date_max = datetime.datetime.strptime(date_max, '%Y-%m-%d')
        # TODO: この方法で utc timezone に変換すると "+00:00" が末尾に付いて、期待するパラメータと形式が異なるため無理やり矯正
        time_min = timezone('UTC').localize(date_min).isoformat()[:-6] + 'Z'  # 'Z' indicates UTC time
        time_max = timezone('UTC').localize(date_max).isoformat()[:-6] + 'Z'  # 'Z' indicates UTC time
    else:
        # TASK: 一週間後とかにしたいけど、日付関連だるいから後回し
        time_min = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        time_max = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time

    # 検索対象の日付一覧を取得
    free_days_in_term = []
    for i in range(0, int((date_max - date_min).days)):
        day = (date_min + datetime.timedelta(days=i)).strftime('%Y-%m-%d')
        free_days_in_term += [day]

    # 指定期間中のスケジュールを取得
    events = calendars.main(time_min, time_max)
    for event in events:
        if event['start']['date'] in free_days_in_term:
            free_days_in_term.remove(event['start']['date'])

    print(free_days_in_term)
    return jsonify(events)


@app.route('/add', methods=['POST'])
def post():
    return redirect(url_for('index'))
