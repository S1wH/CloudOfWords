FROM python:3.10

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY creating.py ./creating.py

CMD python creating.py