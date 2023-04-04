from typing import TYPE_CHECKING

from apps.users.controllers.exceptions import UserNotFound
from apps.users.repository import UserRepository
from apps.users.router import router
from apps.users.serializers import UserDetailSerializer

if TYPE_CHECKING:
    from apps.users.models import Users


@router.get('/users/{account_id}/', response_model=UserDetailSerializer)
async def get_user(account_id: str) -> 'Users':
    user = await UserRepository.get_user_or_none(account_id)

    if not user:
        raise UserNotFound()
    return user
