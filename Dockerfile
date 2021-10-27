FROM ubuntu:16.04

SHELL [ "/bin/bash", "--login", "-c" ]
# Create a non-root user
ARG username=al-khawarizmi
ARG uid=1000
ARG gid=100
ENV USER $username
ENV UID $uid
ENV GID $gid
ENV HOME /home/$USER
RUN adduser --disabled-password \
    --gecos "Non-root user" \
    --uid $UID \
    --gid $GID \
    --home $HOME \
    $USER
    
COPY environment.yml requirements.txt /tmp/
RUN chown $UID:$GID /tmp/environment.yml /tmp/requirements.txt
COPY postBuild /usr/local/bin/postBuild.sh
RUN chown $UID:$GID /usr/local/bin/postBuild.sh && \
    chmod u+x /usr/local/bin/postBuild.sh
COPY docker/entrypoint.sh /usr/local/bin/
RUN chown $UID:$GID /usr/local/bin/entrypoint.sh && \
    chmod u+x /usr/local/bin/entrypoint.sh
    
    
USER $USER
# install miniconda
ENV MINICONDA_VERSION 4.8.2
ENV CONDA_DIR $HOME/miniconda3
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-$MINICONDA_VERSION-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh
# make non-activate conda commands available
ENV PATH=$CONDA_DIR/bin:$PATH
# make conda activate command available from /bin/bash --login shells
RUN echo ". $CONDA_DIR/etc/profile.d/conda.sh" >> ~/.profile
# make conda activate command available from /bin/bash --interative shells
RUN conda init bash

# build the conda environment
ENV ENV_PREFIX $PWD/env
RUN conda update --name base --channel defaults conda && \
    conda env create --prefix $ENV_PREFIX --file /tmp/environment.yml --force && \
    conda clean --all --yes
# run the postBuild script to install any JupyterLab extensions
RUN conda activate $ENV_PREFIX && \
    /usr/local/bin/postBuild.sh && \
    conda deactivate
ENTRYPOINT [ "/usr/local/bin/entrypoint.sh" ]
