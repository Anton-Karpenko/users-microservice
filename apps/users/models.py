from tortoise import fields

from apps.common.models import TimestampMixin
from apps.common.utils.models import id_with_prefix
from apps.users.constants import RoleEnum
from apps.users.constants import StatusEnum


class Users(TimestampMixin):
    id: str = fields.CharField(pk=True, max_length=30, default=id_with_prefix('usr'))
    role: RoleEnum = fields.CharEnumField(RoleEnum, default=RoleEnum.agent)
    account_id: str = fields.CharField(max_length=30, unique=True)
    status: StatusEnum = fields.CharEnumField(StatusEnum, default=StatusEnum.in_progress)

    class Meta:
        table = 'users'

    def __str__(self):
        return self.id
