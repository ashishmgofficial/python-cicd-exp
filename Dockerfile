FROM python:3.9

RUN apt-get update && apt-get -y install gcc libsasl2-dev python-dev
RUN mkdir /app

WORKDIR /app

RUN pip install --upgrade pip wheel setuptools

COPY . .

RUN pip install -r requirements-dev.txt && \
    pip install -r requirements.txt

# ENTRYPOINT [ "" ]
# CMD [ "" ]