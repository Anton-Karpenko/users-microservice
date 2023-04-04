from urllib.parse import urljoin

from fastapi import status

from apps.external_api.accounts.exceptions import AccountAlreadyExist
from apps.external_api.base.api_client import HttpApiClient
from apps.external_api.base.exceptions import ApiException
from config.main import settings


class AccountsApiClient:
    base_url = settings.ACCOUNTS_BACKEND_URL
    client = HttpApiClient()

    register_no_password_url = '/api/register-without-password'  # nosec

    async def create_account_without_pass(self, email: str) -> str:
        try:
            response = await self.client.post(
                urljoin(self.base_url, self.register_no_password_url),
                json={
                    'email': email,
                },
            )
            if response.status_code == status.HTTP_400_BAD_REQUEST:
                raise AccountAlreadyExist()
            return response.json()['id']
        except ApiException:
            raise
