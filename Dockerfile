FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libgl1 libglib2.0-0 libsm6 libxrender1 libxext6 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

# ✅ EXPLICITLY expose port 8000
EXPOSE 8000

# ✅ Run uvicorn on the correct port
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
