# autoinstrumented-python-app
An otel autoinstrumented python app


Python Flask app that listens on `/request` and port `6001` and returns the text "OK".

E.g. Docker run with env variables - 

docker run -it --rm -e OTEL_TRACES_EXPORTER=jaeger-thrift-splunk -e OTEL_EXPORTER_JAEGER_ENDPOINT=https://ingest.<realm>.signalfx.com/v2/trace -e SPLUNK_ACCESS_TOKEN=<token> -e OTEL_PROPAGATORS=b3multi -e OTEL_RESOURCE_ATTRIBUTES=deployment.environment=istio,service.name=test-py-listener --name my-sender -p 6001:6001 harnit/istio-flask-listener:1.0
