FROM python:3-slim
WORKDIR /app
COPY . .
CMD ["python3", "config-vim.py"]
