from fastapi import status
from fastapi.responses import JSONResponse

from apps.common.events.app import kafka_app
from apps.healthcheck.enums import StatusEnum
from apps.healthcheck.router import router
from apps.healthcheck.services.checkers.db import DBHealthchecker
from apps.healthcheck.services.checkers.kafka import KafkaHealthchecker
from apps.healthcheck.services.healthcheck import HealthcheckService

healthchecker = HealthcheckService(conditions=[KafkaHealthchecker(kafka_app), DBHealthchecker()])


@router.get('/api/probes/liveness/')
async def liveness_probe():
    result = await healthchecker.healthcheck()
    return JSONResponse(
        status_code=status.HTTP_200_OK if result.status == StatusEnum.success else status.HTTP_503_SERVICE_UNAVAILABLE,
        content=result.dict(),
    )
