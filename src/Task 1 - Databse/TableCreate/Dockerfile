FROM python:3.7
COPY TableCreater.py /
COPY Setup.config /
COPY /Querys /Querys

RUN pip3 install mysql.connector
RUN pip3 install tqdm
RUN pip3 install names


CMD [ "python3", "-u","./TableCreater.py" ]