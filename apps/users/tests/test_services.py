from unittest import mock

from fastapi import status
from httpx import Response
from nanoid import generate

from apps.users.models import Users
from apps.users.services import InviteAgentStory


class TestInviteAgentStory:
    service_class = InviteAgentStory

    @mock.patch('apps.external_api.accounts.api.HttpApiClient.post')
    @mock.patch('apps.users.services.invite_agent.agent_invited_topic.send')
    async def test_execute__success(self, mocked_topic_send, mocked_api_client):
        mocked_api_client.return_value = Response(status_code=status.HTTP_200_OK, json={'id': generate()})
        mocked_topic_send.return_value = None
        await self.service_class().execute('email@email.com')
        assert mocked_topic_send.call_count == 1

    @mock.patch('apps.external_api.accounts.api.HttpApiClient.post')
    async def test_create_account(self, mocked_api_client):
        expected_id = generate()
        mocked_api_client.return_value = Response(status_code=status.HTTP_200_OK, json={'id': expected_id})
        account_id = await self.service_class()._create_account('email@email.com')
        assert isinstance(account_id, str)
        assert account_id == expected_id

    async def test_create_user(self):
        assert await Users.all().count() == 0
        await self.service_class()._create_user(generate())
        assert await Users.all().count() == 1

    @mock.patch('apps.users.services.invite_agent.agent_invited_topic.send')
    async def test_send_email_message(self, mocked_topic_send):
        mocked_topic_send.return_value = None
        await self.service_class()._send_email_message('email@email.com')
        assert mocked_topic_send.call_count == 1
