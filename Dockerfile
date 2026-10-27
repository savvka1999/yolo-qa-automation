# Берем официальный Python 3.12 (как у тебя в .venv312)
FROM python:3.12-slim-bookworm

# Настройки, чтобы логи сразу выводились в консоль
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Устанавливаем системные библиотеки, которые нужны OpenCV для работы с видео
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую папку внутри контейнера
WORKDIR /app

# Копируем список зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все остальные файлы из папки проекта в контейнер
COPY . .

# Команда по умолчанию: запуск нашего теста
CMD ["pytest", "test_compare_models.py", "-s"]