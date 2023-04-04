from prometheus_client import REGISTRY
from prometheus_client.openmetrics.exposition import CONTENT_TYPE_LATEST
from prometheus_client.openmetrics.exposition import generate_latest
from starlette.responses import Response

from apps.metrics.router import router


@router.get('/metrics')
async def metrics() -> Response:
    return Response(generate_latest(REGISTRY), headers={'Content-Type': CONTENT_TYPE_LATEST})
