FROM python:3.11.0b1-bullseye
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


COPY . /usr/src/app
CMD ["python", "./main.py"]