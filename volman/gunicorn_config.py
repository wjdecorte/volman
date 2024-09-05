import os

from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

workers = int(os.environ.get("WORKERS", 1))
bind = "0.0.0.0:9000"


# noinspection PyUnusedLocal
def post_fork(server, worker):
    resource = Resource.create(attributes={"service.name": "connectors-api"})
    provider = TracerProvider(resource=resource)
    if otlp_exporter_endpoint := os.environ.get("OTLP_EXPORTER_ENDPOINT"):
        parameters = dict(endpoint=otlp_exporter_endpoint)
        exporter = OTLPSpanExporter(**parameters)
    else:
        exporter = ConsoleSpanExporter()
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)
    trace.set_tracer_provider(provider)
