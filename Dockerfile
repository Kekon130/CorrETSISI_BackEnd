FROM python:3.9.16-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python", "app.py" ]