FROM pudo/aleph-base:1.5
ENV DEBIAN_FRONTEND noninteractive

# Begin python festivities
COPY requirements.txt /tmp/requirements.txt
RUN pip install -q --upgrade pip \
  && pip install -q --upgrade setuptools \
  && pip install -q functools32 \
  && pip install -q -r /tmp/requirements.txt

COPY . /aleph
WORKDIR /aleph
ENV ALEPH_SETTINGS /aleph/code4africa_aleph_config.py
RUN pip install git+git://github.com/OpenGazettes/aleph_ke_gazette_crawler.git && \
    pip install -q -e /aleph && \
    rm -rf /aleph/.git && \
    bower --allow-root --quiet install

CMD newrelic-admin run-program gunicorn --workers 1 -b 0.0.0.0:5000 --worker-class gevent --timeout 600 --max-requests 3000 --max-requests-jitter 100 --log-file - --access-logfile - aleph.manage:app
