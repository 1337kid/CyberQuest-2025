FROM debian:trixie-slim

RUN useradd -m bob

RUN apt-get update && apt-get install -y socat \
    && apt clean && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /vuln
COPY vuln /vuln/
WORKDIR /vuln
RUN echo "cyberQuest{71m3_f0R_c0Ff33_40f98b8ae6dd72ef958e7ef3a1d91fde}" > /vuln/flag.txt

EXPOSE 1336

USER bob

CMD ["bash","/vuln/run.sh"]
