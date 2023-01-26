FROM python:3.7-slim-bullseye
RUN \
  apt-get update && \
  apt-get -y install git 
ENV workdir="/code"
WORKDIR ${workdir}
COPY requirements.txt ${workdir}
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD ["bash", "sleep", "infinity"]


