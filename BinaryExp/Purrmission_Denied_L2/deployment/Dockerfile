FROM debian:trixie-slim

RUN useradd -m bob

RUN apt-get update && apt-get install -y socat \
    && apt clean && rm -rf /var/lib/apt/lists/*
    
RUN mkdir /vuln
COPY vuln /vuln/
WORKDIR /vuln
RUN echo "cyberQuest{K177y_54d_4efa0a828c51d4a52a0f61e94414b6f1}" > /vuln/flag.txt

EXPOSE 1338

USER bob

CMD ["bash","/vuln/run.sh"]
