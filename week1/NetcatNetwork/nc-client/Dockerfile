FROM alpine

RUN apk add --no-cache netcat-openbsd

CMD ["sh", "-c", "sleep 5 && echo this is client | nc 172.28.1.10 1337"]
