FROM python:3.7
COPY / /

RUN pip3 install mysql.connector
RUN pip3 install tqdm
RUN pip3 install names
RUN pip3 install flask
RUN pip3 install pycrypto

CMD [ "python3", "-u","./src/main.py" ]