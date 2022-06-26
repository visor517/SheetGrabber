from celery import shared_task
from datetime import datetime
from googleapiclient.discovery import build
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from .models import Order


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

    sheet = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:D10',
        majorDimension='ROWS'
    ).execute()

    # строки без названий колонок
    items = sheet['values'][1:]

    for item in items:

        google_id, order_number, price_us, will_arrive = item
        Order(
            google_id=int(google_id),
            order_number=order_number,
            price_us=int(price_us),
            will_arrive=datetime.strptime(will_arrive, '%d.%m.%Y').date(),
        ).save()

