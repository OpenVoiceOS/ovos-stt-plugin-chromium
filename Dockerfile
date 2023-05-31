FROM debian:buster-slim

RUN apt-get update && \
  apt-get install -y git python3 python3-dev python3-pip curl build-essential

RUN pip3 install flask
RUN pip3 install ovos-plugin-manager
RUN pip3 install ovos-stt-http-server>=0.0.2a6
RUN pip3 install SpeechRecognition==3.8.1

COPY . /tmp/ovos-stt-chromium
RUN pip3 install /tmp/ovos-stt-chromium

ENTRYPOINT ovos-stt-server --engine ovos-stt-plugin-chromium
