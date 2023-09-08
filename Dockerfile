FROM tiangolo/uvicorn-gunicorn:python3.10-slim
WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive
ENV MODULE_NAME=app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN rm -rf /root/.cache
EXPOSE 80
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]