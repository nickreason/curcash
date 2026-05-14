FROM python:3.8-slim
WORKDIR /app
COPY . /app
RUN pip install flask
EXPOSE 3000
CMD ["python", "app.py"]
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:3000/ || exit 1
