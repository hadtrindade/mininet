FROM ubuntu

USER root
WORKDIR /root

COPY docker-entry-point.sh /

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 \
    python3-ryu \
 && chmod +x /docker-entry-point.sh

EXPOSE 6633 6653

ENTRYPOINT ["/docker-entry-point.sh"]