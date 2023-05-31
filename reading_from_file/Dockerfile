FROM python:3.10

RUN pip install --upgrade pip
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY file.txt ./file.txt
COPY reading_file.py ./reading_file.py

CMD python reading_file.py