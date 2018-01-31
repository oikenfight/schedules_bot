### 説明
* Google カレンダーと連携してスケジュールを管理する Bot.
* TIS さんの DialogPlay を使わせてもらいました.

---

### 機能
* 実装済み
    * 指定した期間中のスケジュールを取得
    * 指定した期間中の空き日を取得
* 未実装
    * スケジュールの追加
    * リマインダーを追加
    * スケジュールとリマインダーを分けて取得
    * 期間ではなく特定の日にちのスケジュール・リマインダーを取得
    * 指定した時間でスケジュール・リマインダーを取得（現在は日にちのみ）
    * 今日の残りスケジュール・リマインダーを取得
    * LINE Bot とかで使えるようにして、複数人でリマインダー連携

---

### セットアップ
* 環境
    * Amazon Linux + python3 + flask
* Google Calendar API
    * Google カレンダー API のセットアップについては以下を参照
    * https://dev.classmethod.jp/cloud/google-calendar-api-get-start/
    * https://developers.google.com/google-apps/calendar/quickstart/python?hl=ja
    * 同じディレクトリに quickstart.py と client_secret.json を置いてコマンドを実行しておく必要がありそう
        *
    ```
    $ python quickstart.py
    ```
