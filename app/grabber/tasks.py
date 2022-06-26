from celery import shared_task
from datetime import datetime
from googleapiclient.discovery import build
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from .models import Order
from .utils.get_rate import get_rate

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

    # очистим таблицу
    Order.objects.all().delete()

    # получим курс
    try:
        rate = get_rate()
    except:
        rate = None

    for item in items:
        google_id, order_number, price_us, will_arrive = item
        if rate:
            price_ru = round(float(price_us) * rate, 2)
        else:
            price_ru = None

        Order(
            google_id=int(google_id),
            order_number=order_number,
            price_us=round(float(price_us), 2),
            price_ru=price_ru,
            will_arrive=datetime.strptime(will_arrive, '%d.%m.%Y').date(),
        ).save()
