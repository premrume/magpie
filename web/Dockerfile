FROM python:3.6.1

# Info
LABEL maintainer="Magpie" \
      version="1"


#  As ROOT
COPY requirements.txt /tmp
RUN groupadd flaskgroup \
 && useradd -m -g flaskgroup -s /bin/bash flask \ 
 && mkdir -p /var/scratch \
 && chown -R flask:flaskgroup /var/scratch \
 && pip install --upgrade pip \  
 && cd /tmp \
 && pip install --no-cache-dir -r requirements.txt 

# Install the app as user  as user flask
# see .dockerignore
USER flask
WORKDIR /var/scratch
COPY .  /var/scratch

# Runtime environment as user flask
RUN mkdir -p /var/scratch/uploads
VOLUME /var/scratch/uploads
EXPOSE 5000
ENV FLASK_APP run.py
ENV FLASK_ENV development
ENV FLASK_DEBUG 1
CMD flask run --host=0.0.0.0 --port=5000

# Example to test this image:
# mkdir /whatever/data
# docker build -t this
# docker run -t -p 5000:5000 -v /whatever/data:/var/scratch/uploads this

