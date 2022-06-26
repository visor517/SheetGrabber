import httplib2
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


CREDENTIALS_FILE = './google_api_key.json'
spreadsheet_id = '1mx8zoY2IGLzVVWw-yYnxtuHW0ejE7QYV8neu39rmsME'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = build('sheets', 'v4', http=httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='A1:D10',
    majorDimension='ROWS'
).execute()
print(values)
exit()
