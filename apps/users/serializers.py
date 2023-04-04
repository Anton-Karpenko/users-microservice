from pydantic import BaseModel
from pydantic import EmailStr
from tortoise.contrib.pydantic import pydantic_model_creator

from apps.users.models import Users


class EmailSerializer(BaseModel):
    email: EmailStr


UserDetailSerializer = pydantic_model_creator(
    Users, name='UserDetailSerializer', include=('id', 'role', 'account_id', 'status')
)
