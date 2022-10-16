#FROM python:3.10-alpine as base
FROM debian:stable


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR false
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null


## For chromedriver installation: curl/wget/libgconf/unzip

RUN apt-get update -y && apt-get install -y wget curl unzip libgconf-2-4
## For project usage: python3/python3-pip/chromium/xvfb
RUN apt-get update -y && apt-get install -y chromium xvfb python3 python3-pip
RUN pip3 install --upgrade pip


WORKDIR /app

COPY ./envs ./envs
COPY ./utils ./utils
COPY ./db ./db

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
#CMD sh -c "python orm.py"

#FROM base as db
#COPY db ./db
#CMD sh -c "python orm.py"

FROM base as worker
COPY worker ./worker
COPY run.sh .
CMD /bin/bash run.sh
CMD sh -c "python3 -m worker"

FROM base as web
COPY web ./web
CMD ["python", "db/orm.py"]

CMD ["uvicorn", "web.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]




