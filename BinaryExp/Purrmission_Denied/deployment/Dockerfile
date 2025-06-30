FROM debian:trixie-slim

RUN useradd -m bob
RUN apt update && apt install -y socat && apt clean
RUN mkdir /vuln
COPY vuln /vuln/
WORKDIR /vuln

EXPOSE 1337

CMD ["bash","/vuln/run.sh"]