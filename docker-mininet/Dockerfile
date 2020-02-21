FROM ubuntu

USER root
WORKDIR /root

COPY docker-entrypoint.sh /

RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    iproute2 \
    iputils-ping \
    mininet \
    net-tools \
    openvswitch-switch \
    openvswitch-testcontroller \
    tcpdump \
    vim \
    x11-xserver-utils \
    xterm \
    netcat-openbsd \
 && rm -rf /var/lib/apt/lists/* \
 && chmod +x /docker-entrypoint.sh

EXPOSE 6633 6653 6640
ENTRYPOINT ["/docker-entrypoint.sh"]



