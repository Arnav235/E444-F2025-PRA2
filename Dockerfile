FROM python:3.9-slim

ENV FLASK_APP=hello.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT ["flask"]
CMD ["run"]