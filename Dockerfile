FROM python:3.11-slim
ENV PIP_DISABLED_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["flask", "--app", "main", "run", "--host", "0.0.0.0", "--port", "8000"]