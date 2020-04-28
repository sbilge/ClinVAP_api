FROM continuumio/miniconda3:4.8.2

LABEL maintainer="bilge.sueruen@uni-tuebingen.de"

# Add Watchdog module to conda base for start_nextflow.py script
RUN conda install -y -c conda-forge watchdog=0.10.2

# install some required packages including java 
RUN mkdir -p /usr/share/man/man1

RUN apt-get -y update && \
    apt-get -y upgrade && \
    apt-get install -y apt-utils procps curl default-jdk vim && \
    apt-get clean -y


# Install Nextflow
RUN curl -fsSL get.nextflow.io | bash && \
    mv nextflow /usr/bin


# Install Git
RUN apt-get install git

# Create nextflow directories
RUN mkdir /nextflow_pipeline
RUN mkdir /nextflow_pipeline/uploads
RUN mkdir /nextflow_pipeline/downloads
RUN mkdir /nextflow_pipeline/work

WORKDIR /nextflow_pipeline

# Copy nextflow start script and make it executable
COPY start_nextflow.py .
RUN chmod +x start_nextflow.py

# Clone conda branch of nextflow pipeline
RUN git clone --single-branch --branch conda https://github.com/sbilge/nf-core-clinvap.git

# Create conda env
RUN conda env create -f nf-core-clinvap/environment.yml && conda clean -a

# Add conda installation dir to PATH (instead of doing 'conda activate')
ENV PATH /opt/conda/envs/nf-core-clinvap-1.0dev/bin:$PATH

# Add entrypoint to start nextflow 
ENTRYPOINT [ "start_nextflow.py" ]
