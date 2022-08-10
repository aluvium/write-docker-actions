FROM python:3
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /cats
COPY . .
CMD [ "/bin/python3", "src/main.py" ]
