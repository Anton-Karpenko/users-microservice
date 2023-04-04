from apps.common.events.records import InvitedAgent
from apps.common.events.topics import agent_invited_topic
from apps.external_api import AccountsApiClient
from apps.users.repository import UserRepository
from apps.users.serializers import EmailSerializer


class InviteAgentStory:
    """
    Story to invite an agent to join the platform via email.
    """

    async def execute(self, email: str) -> None:
        email = EmailSerializer(email=email).email
        account_id = await self._create_account(email)
        await self._create_user(account_id)
        await self._send_email_message(email)

    @staticmethod
    async def _create_account(email: str) -> str:
        return await AccountsApiClient().create_account_without_pass(email)

    @staticmethod
    async def _create_user(account_id: str) -> None:
        await UserRepository.create_agent(account_id=account_id)

    @staticmethod
    async def _send_email_message(email: str) -> None:
        agent = InvitedAgent(email=email)
        await agent_invited_topic.send(value=agent)
