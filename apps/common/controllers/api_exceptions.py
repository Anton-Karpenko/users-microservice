from typing import Any

from fastapi import HTTPException
from fastapi import status


class BaseAPIException(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = 'A server error occurred.'

    def __init__(self, status_code: int | None = None, detail: Any = None, headers: dict[str, Any] | None = None):
        if status_code is None:
            status_code = self.status_code
        if detail is None:
            detail = self.detail
        super().__init__(status_code=status_code, detail=detail, headers=headers)
