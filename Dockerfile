FROM alpine

COPY . /app
WORKDIR /app
RUN apk update ; apk add python3 py-pip
RUN pip install --upgrade pip ; pip install -r requirements.txt

EXPOSE 5080

CMD ["python3", "app.py"]
