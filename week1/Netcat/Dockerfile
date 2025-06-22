FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -ms /bin/bash user

RUN apt update && apt install -y \
    netcat-traditional \
    bash \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/editable && \
    chown user:user /home/editable && \
    echo "Welcome. Edit this file." > /home/editable/info.txt

WORKDIR /home/editable

EXPOSE 9001

CMD ["bash", "-c", "nc.traditional -lkp 9001 -e su -s /bin/bash user"]
