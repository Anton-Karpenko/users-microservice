import faust

from config.main import settings

kafka_app = faust.App(
    settings.KAFKA_APPLICATION_ID,
    broker=settings.KAFKA_BROKER_URL,
)
