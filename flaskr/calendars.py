from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from flaskr import config

import datetime

SCOPES = config.SCOPES
CLIENT_SECRET_FILE = config.CLIENT_SECRET_FILE
APPLICATION_NAME = config.APPLICATION_NAME
CALENDAR_ID = config.CALENDAR_ID
API_KEY = config.API_KEY

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def main(time_min, time_max):
    """Shows basic usage of the Google Calendar API.

    Creates a Google Calendar API service object and outputs a list of the next
    10 events on the user's calendar.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)

    if not time_min:
        time_min = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    # if not time_max:
    #     # TODO: time_max の形式を揃える
    #     time_max = time_max + 'Z'  # 'Z' indicates UTC time

    # ここで取ってくるイベントを指定
    eventsResult = service.events().list(
        calendarId=CALENDAR_ID,
        # timeMin=time_min,
        timeMax=time_max,
        maxResults=20,
        singleEvents=True,
        orderBy='startTime',
        key=API_KEY,
    ).execute()

    events = eventsResult.get('items', [])
    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

    return events


def get_schedules(start_date, last_date):
    """
    期間中のスケジュール情報を取得する
    :param start_date:
    :param
    :return:
    """


if __name__ == '__main__':
    main()
