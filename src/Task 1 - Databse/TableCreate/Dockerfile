FROM python:3.7
COPY TableCreater.py /
COPY Setup.config /
COPY /Querys /

RUN pip3 install mysql.connector
RUN pip3 install tqdm
RUN pip3 install names
RUN pip3 install hashlib
RUN pip3 install random

CMD [ "python3", "-u","./TableCreater.py" ]