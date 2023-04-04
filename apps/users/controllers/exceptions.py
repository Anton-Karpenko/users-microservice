from fastapi import status

from apps.common.controllers.api_exceptions import BaseAPIException


class UserNotFound(BaseAPIException):
    status_code = status.HTTP_404_NOT_FOUND
    detail = 'User not found.'
