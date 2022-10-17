FROM debian:stable as base







## For chromedriver installation: curl/wget/libgconf/unzip

RUN apt-get update -y && apt-get install -y wget curl unzip libgconf-2-4
## For project usage: python3/python3-pip/chromium/xvfb
RUN apt-get update -y && apt-get install -y chromium xvfb python3 python3-pip
RUN pip3 install --upgrade pip


RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PIP_NO_CACHE_DIR false
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null


WORKDIR /app

COPY ./envs ./envs
COPY ./utils ./utils
COPY ./db ./db

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
#CMD sh -c "python orm.py"
#CMD ['python3', './db/orm.py']
CMD ['python3', './db/orm.py']

#CMD ["createdb", "googlegmail"]

#FROM base as db
#COPY db ./db
#CMD sh -c "python orm.py"
FROM base as worker

COPY worker ./worker
COPY run.sh .
CMD /bin/bash run.sh

#CMD sh -c "python3 -m worker"

FROM base as web

COPY web ./web

CMD ["uvicorn", "web.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]







#CMD ['python3', './db/orm.py']




