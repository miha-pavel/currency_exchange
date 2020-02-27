FROM python:3.7.6
# ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install -y\
    python-dev \
    python-setuptools \
    && apt-get clean

RUN mkdir /currency_exchange

WORKDIR /currency_exchange

COPY requirements.txt /currency_exchange/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /currency_exchange/