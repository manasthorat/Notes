import pytest
from main import connect

@pytest.fixture
def user():
    return "admin"

@pytest.fixture
def connection(user):
    return connect(user)

def test_connection(connection):
    assert "admin" in connection
