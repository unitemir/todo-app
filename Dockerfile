FROM python:3.9
WORKDIR /code

# set env
ENV PYTHONUNBUFFERED=1

# install dependencies
RUN apt-get update && pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/