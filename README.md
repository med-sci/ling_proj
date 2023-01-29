# Corpora filtering tool

Corpora filtering tool based on [OpusFilter](https://github.com/Helsinki-NLP/OpusFilter) with some custom filters

## Getting Started

### Dependencies

* Linux
* Docker
* Nvidia-docker, nvidia drivers and NVIDIA Container Toolkit for gpu computations

### Installing

* Clone [repository](https://github.com/med-sci/ling_proj.git)
* Customize ```config.yaml``` file
* Run ```bash run.sh``` for docker image building and starting of a container task

### Config.yaml specifications

* Replace predefined input and output path to own in all parts of YAML configuration file or just test it running on example data
```yaml
    inputs:
      - ./data/Example.en-ru.en
      - ./data/Example.en-ru.ru
    outputs:
      - ./results/NoDuplicates.en-ru.en
      - ./results/NoDuplicates.en-ru.ru
```
* Change any parameters in filters with respect to [OpusFilter documentation](https://helsinki-nlp.github.io/OpusFilter/)
* For setting up custom filters follow the information below

## Custom filters list
* ```BERTCosineSimilarity``` filter calculates cosine similarity between sentences pairs based on representation from [pre-trained multilingual BERT model](https://huggingface.co/bert-base-multilingual-cased). Acceptance criteria for a score is to be greater then ```threshold``` (default value is 0.2).


## Authors

Contributors names and contact info

[@Yury Kashkur]()

## Version History

* 0.0.1
    * Implementation of custom BERT filter
* 0.0.2
    * GPU computation set up