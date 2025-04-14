# Build Stage
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Final Stage
FROM python:3.11-alpine
WORKDIR /app
COPY --from=builder /install /usr/local
COPY app.py .
RUN adduser -D flaskuser
USER flaskuser
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]