FROM python:3.13.0

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install - requirements.text

COPY . .

CMD["python3", "manage.py", "runserver", "0.0.0.0:8000"]