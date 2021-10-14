FROM python:3.7

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY server.py ./

RUN splunk-py-trace-bootstrap

CMD splunk-py-trace python3 server.py
