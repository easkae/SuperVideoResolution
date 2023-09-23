FROM ubuntu:latest
LABEL authors="zabar"

ENTRYPOINT ["top", "-b"]