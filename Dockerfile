FROM python:3

WORKDIR /usr/src/app

COPY . ./
# RUN pip install build
# CMD python3 -m build .
RUN pip install -r requirements.txt
CMD strawberry server src.schema