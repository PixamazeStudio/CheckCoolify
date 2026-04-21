FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:3000"]
