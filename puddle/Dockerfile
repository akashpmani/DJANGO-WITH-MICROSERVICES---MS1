FROM python

ENV PYTHONBUFFERED=1

WORKDIR /puddle

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000
