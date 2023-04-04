from apps.common.tests.async_factory import AsyncFactory
from apps.users.models import Users


class UserFactory(AsyncFactory):
    class Meta:
        model = Users
