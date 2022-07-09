FROM mcr.microsoft.com/playwright:focal

RUN apt-get update && apt-get install -y python3-pip

WORKDIR /usr/src/app

COPY * ./
RUN pip install build
RUN python3 -m pip install -r requirements.txt
