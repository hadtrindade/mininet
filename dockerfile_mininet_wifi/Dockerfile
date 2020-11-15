FROM ubuntu:16.04

USER root
WORKDIR /root

COPY docker-entrypoint.sh /

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    sudo \
    iproute2 \
    iputils-ping \
    net-tools \
    tcpdump \
    vim \
    git \
    x11-xserver-utils \
    xterm \
    python-setuptools \
    python-matplotlib \
    netcat-openbsd \
    ca-certificates \
    lsb-release \
 && git clone https://github.com/intrig-unicamp/mininet-wifi \
 && cd mininet-wifi \
 && util/install.sh -Wlnfv \
 && rm -rf /var/lib/apt/lists/* \
 && chmod +x /docker-entrypoint.sh


EXPOSE 6633 6653 6640
ENTRYPOINT ["/docker-entrypoint.sh"]



