FROM python:3.11-slim

WORKDIR /app

COPY app.py .

RUN useradd -m -u 1001 appuser
RUN mkdir -p /data && chown -R appuser:appuser /data

USER appuser

EXPOSE 8000

CMD ["python3", "app.py"]