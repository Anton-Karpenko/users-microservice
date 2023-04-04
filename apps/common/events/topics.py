from apps.common.events.app import kafka_app
from apps.common.events.records import InvitedAgent
from config.main import settings

agent_invited_topic = kafka_app.topic(
    settings.KAFKA_INVITED_AGENT_TOPIC,
    value_type=InvitedAgent,
)
