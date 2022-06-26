from celery import shared_task
from googleapiclient.discovery import build
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = './google_api_key.json'
spreadsheet_id = '1mx8zoY2IGLzVVWw-yYnxtuHW0ejE7QYV8neu39rmsME'


@shared_task
def get_sheet():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    http_auth = credentials.authorize(httplib2.Http())
    service = build('sheets', 'v4', http=http_auth)

    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:D10',
        majorDimension='ROWS'
    ).execute()

    return values
