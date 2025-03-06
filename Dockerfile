FROM locustio/locust
WORKDIR /home/locust
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY docker-locust.py locustfile.py
COPY . .
RUN echo 'locust -f /home/locust/locustfile.py --headless -u 100 -r 50 -l 5m -H ${TARGET}' > /home/locust/entrypoint.sh
ENTRYPOINT /bin/sh /home/locust/entrypoint.sh
