from apps.users.constants import RoleEnum
from apps.users.models import Users


class UserRepository:
    @staticmethod
    async def _create_user(data: dict[str, str]) -> Users:
        return await Users.create(**data)  # type: ignore

    @classmethod
    async def create_agent(cls, account_id: str) -> Users:
        data = {'account_id': account_id, 'role': RoleEnum.agent}
        return await cls._create_user(data=data)

    @classmethod
    async def get_user_or_none(cls, account_id: str) -> Users | None:
        return await Users.get_or_none(account_id=account_id)
