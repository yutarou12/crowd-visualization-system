FROM python:3.10-slim

WORKDIR /app

# 必要パッケージ
RUN apt update && apt install -y \
    libglib2.0-0 \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/requirements.txt

RUN python -m pip install --upgrade pip setuptools wheel
RUN if [ -f /app/requirements.txt ]; then python -m pip install --no-cache-dir -r /app/requirements.txt; fi

ENTRYPOINT ["python", "main-yoru.py"]