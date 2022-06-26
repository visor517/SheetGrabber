# SheetGrabber

## Запуск

### 1. Запуск контейнеров
```
docker-compose up --build
```

### 2. Создать админа
при запущенном docker-compose.
```
python app/manage.py createsuperuser --settings=sheetgrabber.settings.debug_ext
```

### 3. Создать периодическую задачу в админке
Здесь будет скрин
1. Сздать новую задачу Periodic tasks
2. Придумать название
3. Вызывать задачу grabber.tasks.get_sheet
4. Установить интервал срабатывания

### =====
Google sheet
https://docs.google.com/spreadsheets/d/1mx8zoY2IGLzVVWw-yYnxtuHW0ejE7QYV8neu39rmsME/edit#gid=0

Разрабатывалось на:
Python 3.9.12
