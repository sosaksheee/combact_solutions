FROM python:3.10-slim

WORKDIR /app

COPY chatbot.py .

RUN pip install --no-cache-dir langgraph

CMD ["python", "chatbot.py"]
