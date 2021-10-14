FROM python:3.8-slim-buster

WORKDIR /usr/src/app

COPY req.txt req.txt
RUN pip3 install -r req.txt

COPY . .

CMD ["python", "main.py"]