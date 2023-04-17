FROM python:3.8

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python","./app.py"]