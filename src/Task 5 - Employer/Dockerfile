FROM python:3.7
COPY / /

RUN pip3 install mysql.connector
RUN pip3 install tqdm
RUN pip3 install names
RUN pip3 install requests

CMD [ "python3", "-u","./main.py" ]