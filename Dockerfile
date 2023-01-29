FROM nvidia/cuda:11.3.0-runtime-ubuntu20.04
  
ENV workdir="/code"
ENV PYTHONPATH=$PYTHONPATH:$(pwd)/customfilters

ARG DEBIAN_FRONTEND=noninteractive 

WORKDIR ${workdir}

COPY requirements.txt ${workdir}
COPY config.yaml ${workdir}

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    vim \
    build-essential \
    screen \
    python3.8 \
    python3-distutils \ 
    python3-pip \ 
    python3-apt \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN python3 -m laserembeddings download-models

CMD ["opusfilter", "config.yaml"]


