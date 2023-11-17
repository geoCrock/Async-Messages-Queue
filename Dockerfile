FROM ubuntu:latest
LABEL authors="geo"

ENTRYPOINT ["top", "-b"]