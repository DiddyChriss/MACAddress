FROM python:3.8

RUN mkdir /mac
WORKDIR /mac
COPY . /mac/
RUN pip install -r requirements.txt

CMD ['python', 'MACAddress.py']