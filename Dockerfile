FROM python:3.11

COPY manage.py /app/
COPY db.sqlite3 /app/
COPY PEAMS /app/
COPY peams_app /app/
COPY staticfiles /app/

WORKDIR /app

RUN pip install django

CMD [ "python", "manage.py", "runserver"]