# docker build . -t opus-filter:0.0.2

NVIDIA_DOCKER_INSTALLED="$(apt list --installed | grep nvidia-docker)"

if [ ! -z "${NVIDIA_DOCKER_INSTALLED}" ];
    then
    echo "RUNING NVIDIA-DOCKER"
    nvidia-docker run -it -v ${PWD}:/code opus-filter:0.0.2
else
    echo "RUNING DOCKER WITHOUT CUDA"
    echo "For GPU computations, please, install nvidia-docker"
    docker run -it -v ${PWD}:/code opus-filter:0.0.2
fi