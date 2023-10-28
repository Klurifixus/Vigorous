FROM python:3.11-slim-bookworm
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN npm install jquery


COPY . .
CMD ["python", "app.py"]