# api_yamdb

api_yamdb

## Как запустить проект:

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/shtrihh88/api_yamdb.git
```

```
cd api_yamdb
```

### Cоздать и активировать виртуальное окружение
под Windows:

```
python -m venv venv
```

```
venv\Scripts\activate
```

под Linux
```
python3 -m venv env
```

```
source env/bin/activate
```

### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
python manage.py makemigrations
python manage.py migrate
```

### Запустить проект:

```
python3 manage.py runserver
```
