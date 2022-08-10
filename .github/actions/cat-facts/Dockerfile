FROM python:3
RUN apt-get update -y \ 
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /cats
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./src/main.py"]
