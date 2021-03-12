FROM ubuntu:20.04

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONUNBUFFERED=1
ENV APP_HOME /usr/src/app

WORKDIR /$APP_HOME

##install python 3.7 on Debian 9
RUN apt-get update
RUN apt-get install -y python3 python3-pip libpq-dev
#RUN apt-get update && apt-get install -y wget

#WORKDIR /tmp/
#RUN wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tar.xz
#RUN tar -xvf Python-3.7.9.tar.xz
#RUN cd Python-3.7.9/ && \ 
#    ./configure && \ 
#    make && \ 
#    make install && \
#    update-alternatives --install /usr/bin/python python /usr/local/bin/python3.7 10



#ln -s /usr/share/pyshared/lsb_release.py /usr/local/lib/python3.7/site-packages/lsb_release.py
#pip3 install --upgrade pip

#copy all files less venv folder
COPY . $APP_HOME/
#install python requirements
RUN pip3 install -r ./requirements.txt

EXPOSE 8080
CMD flask run
