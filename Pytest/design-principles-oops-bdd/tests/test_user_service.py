from src.services.user_service import UserService
from src.models.user import User


def test_user_registration():
    service = UserService()
    user = User(1, "test@example.com")

    result = service.register(user)

    assert "registered" in result
