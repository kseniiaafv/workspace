# Инструкции

## Активация виртуального окружения
```bash
source .venv/bin/activate
.\.venv\Scripts\Activate.ps1
```

Когда мы меняем models.py
```bash
python manage.py makemigrations
python manage.py migrate
```

Создание суперпользователя
```bash
python manage.py createsuperuser
```

Запуск сервера
```bash
python manage.py runserver
```