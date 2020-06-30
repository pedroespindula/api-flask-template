FROM python:3.7

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python src/__main__.py
