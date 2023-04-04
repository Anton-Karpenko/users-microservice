from fastapi import status
from nanoid import generate

from apps.users.tests.factories import UserFactory


class TestUsersController:
    async def test_should_return_200(self, client):
        account_id = generate()
        await UserFactory(account_id=account_id)
        url = client.app.url_path_for('get_user', account_id=account_id)
        response = await client.get(url)
        assert response.status_code == status.HTTP_200_OK

    async def test_should_return_404(self, client):
        url = client.app.url_path_for('get_user', account_id=generate())
        response = await client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
