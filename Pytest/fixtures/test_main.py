from main import usermanager
import pytest

@pytest.fixture
def user_manager():
    return usermanager()

def test_add_user(user_manager):
    assert user_manager.add_user("manas" , "manas@gmail.com") == True
    assert user_manager.get_user_email("manas") == "manas@gmail.com"

def test_add_existing_user_raises_error(user_manager):
    user_manager.add_user("manas" , "manas@gmail.com")
    with pytest.raises(ValueError):
        user_manager.add_user("manas" , "manas@gmail.com")