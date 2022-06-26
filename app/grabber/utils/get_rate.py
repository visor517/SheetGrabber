from datetime import date
import requests
import xml.etree.ElementTree as ET


def get_rate():
    day = date.today().strftime('%d/%m/%Y')
    response = requests.get(f'https://www.cbr.ru/scripts/XML_daily.asp?date_req={day}')
    xml = response.content.decode(encoding='windows-1251')
    root_node = ET.fromstring(xml)

    for tag in root_node.findall('Valute'):
        valute_id = tag.get('ID')
        if valute_id == 'R01235':
            result = tag.find('Value').text
            return float(result.replace(',', '.'))
