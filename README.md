# SheetGrabber

## Запуск

### Запуск проекта
```
docker-compose up --build
```

### Создать админа
при запущенном docker-compose
```
python app/manage.py createsuperuser --settings=sheetgrabber.settings.debug_ext
```


### =====
Google sheet
https://docs.google.com/spreadsheets/d/1mx8zoY2IGLzVVWw-yYnxtuHW0ejE7QYV8neu39rmsME/edit#gid=0

Разрабатывалось на:
Python 3.9.12
