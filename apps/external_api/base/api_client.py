import logging

import httpx

from apps.external_api.base.exceptions import ApiException
from config.main import settings

logger = logging.getLogger(__name__)


class HttpApiClient:
    _default_request_error = 'An error occurred while requesting url=%s.'

    async def post(self, url: str, *args, **kwargs):
        async with httpx.AsyncClient(headers=kwargs.pop('headers', {})) as client:
            try:
                response = await client.post(url, timeout=settings.DEFAULT_API_TIMEOUT, *args, **kwargs)
                logger.info(
                    'Got response from url=%s, status=%s, with data=%s' % (url, response.status_code, response.json())
                )
                return response
            except httpx.RequestError as exc:
                raise ApiException(self._default_request_error % exc.request.url)

    async def get(self, url: str, *args, **kwargs):
        async with httpx.AsyncClient(headers=kwargs.pop('headers', {})) as client:
            try:
                response = await client.get(url, timeout=settings.DEFAULT_API_TIMEOUT, *args, **kwargs)
                logger.info(
                    'Got response from url=%s, status=%s, with data=%s' % (url, response.status_code, response.json())
                )
                return response
            except httpx.RequestError as exc:
                raise ApiException(self._default_request_error % exc.request.url)

    async def put(self, url: str, *args, **kwargs):
        async with httpx.AsyncClient(headers=kwargs.pop('headers', {})) as client:
            try:
                response = await client.put(url, timeout=settings.DEFAULT_API_TIMEOUT, *args, **kwargs)
                logger.info(
                    'Got response from url=%s, status=%s, with data=%s' % (url, response.status_code, response.json())
                )
                return response
            except httpx.RequestError as exc:
                raise ApiException(self._default_request_error % exc.request.url)

    async def patch(self, url: str, *args, **kwargs):
        async with httpx.AsyncClient(headers=kwargs.pop('headers', {})) as client:
            try:
                response = await client.patch(url, timeout=settings.DEFAULT_API_TIMEOUT, *args, **kwargs)
                logger.info(
                    'Got response from url=%s, status=%s, with data=%s' % (url, response.status_code, response.json())
                )
                return response
            except httpx.RequestError as exc:
                raise ApiException(self._default_request_error % exc.request.url)

    async def delete(self, url: str, *args, **kwargs):
        async with httpx.AsyncClient(headers=kwargs.pop('headers', {})) as client:
            try:
                response = await client.delete(url, timeout=settings.DEFAULT_API_TIMEOUT, *args, **kwargs)
                logger.info(
                    'Got response from url=%s, status=%s, with data=%s' % (url, response.status_code, response.json())
                )
                return response
            except httpx.RequestError as exc:
                raise ApiException(self._default_request_error % exc.request.url)
