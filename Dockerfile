FROM python:3.11-slim

WORKDIR /app

# копируем requirements.txt из корня в контейнер
COPY requirements.txt .

# ставим зависимости
RUN pip install --no-cache-dir -r requirements.txt

# копируем весь код приложения
COPY app/ /app/

CMD ["python", "main.py"]
