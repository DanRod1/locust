FROM locustio/locust
WORKDIR /home/locust
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY locustfile.py locustfile.py
COPY . .
RUN echo 'locust -f /home/locust/locustfile.py --headless -H http://192.168.0.2' > /home/locust/entrypoint.sh
RUN chmod +x /home/locust/entrypoint.sh
ENTRYPOINT /home/locust/entrypoint.sh
