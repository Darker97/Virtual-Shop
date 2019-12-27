FROM python:3.7
COPY TableCreater.py /
COPY Setup.config /
COPY query.sql /

RUN pip3 install mysql.connector
CMD [ "python3", "-u","./CreateDatabase.py" ]