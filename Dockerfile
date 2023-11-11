FROM --platform=linux/amd64 python:3.11

WORKDIR /database

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "database.api:app", "--host", "0.0.0.0", "--port", "8000"]