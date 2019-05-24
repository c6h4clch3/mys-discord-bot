from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = [
    'https://www.googleapis.com/auth/calendar',
]
CALENDAR_ID = ''
with open('./calendar_id') as f:
    CALENDAR_ID = f.read()


def addCalendar(title, times, description):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            creds = Credentials.from_service_account_file('./svc.json').with_scopes(SCOPES)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    event = {
        "start": {"dateTime": times[0].isoformat()},
        "end": {"dateTime": times[1].isoformat()},
        "summary": title,
        "description": description,
        "transparency": "transparent",
        "reminders": {
            "useDefault": False,
            "overrides": []  # 通知を無効にするにはこのようにする
        }
    }

    # Call the Calendar API
    # pylint: disable=E1101
    service.events().insert(calendarId=CALENDAR_ID,
                            body=event).execute()

