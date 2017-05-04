FROM kbase/kbase:sdkbase.latest
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

RUN apt-get update -y

RUN sudo apt-get install -y python-dev libffi-dev libssl-dev
RUN pip install --upgrade pip
RUN pip install cffi --upgrade
RUN pip install pyopenssl --upgrade
RUN pip install ndg-httpsclient --upgrade
RUN pip install pyasn1 --upgrade

RUN pip install requests --upgrade \
    && pip install 'requests[security]' --upgrade \
    && pip install ipython \
    && apt-get install -y nano \
    && pip install psutil \
    && apt-get install perl-modules libperl4-corelibs-perl

# -----------------------------------------

# Install A5
RUN cd /opt \
    && git clone https://github.com/levinas/a5.git

ENV PATH $PATH:/opt/a5/bin

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod -R a+rw /kb/module

WORKDIR /kb/module

RUN make

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
