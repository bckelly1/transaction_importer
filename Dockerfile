FROM python:3.11

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "./src/app.py"]
