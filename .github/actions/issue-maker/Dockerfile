FROM node:slim
RUN apt-get update \ 
    && apt-get clean \ 
    && rm -fr /var/lib/apt/lists/*
WORKDIR /app
COPY . .
RUN  npm install
CMD ["sh", "-c", "node /app/src/index.js"]
