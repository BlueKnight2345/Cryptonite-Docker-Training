FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN useradd -ms /bin/bash user

RUN apt update && apt install -y \
    socat \
    bash \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/editable && \
    chown user:user /home/editable && \
    echo "test" > /home/editable/info.txt

WORKDIR /home/editable

CMD ["socat", "TCP-LISTEN:9001,reuseaddr,fork", "EXEC:'su -s /bin/bash user',pty,stderr,setsid,sigint,sane"]
