from unittest import mock

import pytest
from fastapi import status
from httpx import Response
from nanoid import generate

from apps.external_api import AccountsApiClient
from apps.external_api.accounts.exceptions import AccountAlreadyExist
from apps.external_api.base.exceptions import ApiException


@pytest.mark.asyncio
class TestAccountsApiClient:
    @mock.patch('apps.external_api.accounts.api.HttpApiClient.post')
    async def test_create_account_without_pass__should_return_account_id(self, mocked_api_client):
        response_json = {'id': generate()}
        mocked_api_client.return_value = Response(status_code=status.HTTP_201_CREATED, json=response_json)
        account_id = await AccountsApiClient().create_account_without_pass(email='test@email.com')
        assert account_id == response_json['id']

    @mock.patch('apps.external_api.accounts.api.HttpApiClient.post')
    async def test_create_account_without_pass__should_raise_account_already_exist(self, mocked_api_client):
        mocked_api_client.return_value = Response(
            status_code=status.HTTP_400_BAD_REQUEST, json={'detail': 'Account already exist'}
        )
        with pytest.raises(AccountAlreadyExist):
            await AccountsApiClient().create_account_without_pass(email='test@email.com')

    @mock.patch('apps.external_api.accounts.api.HttpApiClient.post')
    async def test_create_account_without_pass__should_raise_api_error(self, mocked_api_client):
        mocked_api_client.side_effect = ApiException
        with pytest.raises(ApiException):
            await AccountsApiClient().create_account_without_pass(email='test@email.com')
