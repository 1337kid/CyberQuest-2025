FROM debian:trixie-slim

RUN useradd -m bob

RUN apt-get update && apt-get install -y socat \
    && apt clean && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /vuln
COPY vuln /vuln/
WORKDIR /vuln
RUN echo "cyberQuest{U53_fg375_br0_3d33044b69d6314e6cb6f6924126d144}" > /vuln/flag.txt

EXPOSE 1337

USER bob

CMD ["bash","/vuln/run.sh"]
