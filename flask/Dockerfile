FROM continuumio/miniconda3:4.7.12

LABEL author="bilge.sueruen@uni-tuebingen.de" \
    description="Docker image to start flask application"

WORKDIR /app

ADD . /app

RUN conda env create -f environment.yml && conda clean -a

# RUN conda activate api_app

ENV PATH /opt/conda/envs/api_app/bin:$PATH

CMD ["uwsgi", "app.ini"]