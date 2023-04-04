from nanoid import generate

from apps.users.constants import RoleEnum
from apps.users.constants import StatusEnum
from apps.users.repository import UserRepository
from apps.users.tests.factories import UserFactory


class TestUserRepository:
    repository = UserRepository

    async def test_create_agent(self):
        account_id = generate()
        agent = await self.repository.create_agent(account_id)
        assert agent.account_id == account_id
        assert agent.role == RoleEnum.agent
        assert agent.status == StatusEnum.in_progress

    async def test_get_user_or_none__should_return_1(self):
        account_id = generate()
        await UserFactory(account_id=account_id)
        user = await self.repository.get_user_or_none(account_id)
        assert user is not None

    async def test_get_user_or_none__should_return_none(self):
        account_id = generate()
        user = await self.repository.get_user_or_none(account_id)
        assert user is None
