FROM python:3.12

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "todo_app.wsgi:todo"]
