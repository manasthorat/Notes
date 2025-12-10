import pytest
from main import database

@pytest.fixture
def db():
    """Fixture to set up and tear down a database connection."""

    database_instance = database()
    yield database_instance # Provide the fixture value
    database_instance.close() # Teardown code

def test_add_user(db: database):
    db.add_user("user1", "Alice")
    assert db.get_user("user1") == "Alice"

def add_duplicate_user_raises_error(db):
    db.add_user("user1", "Alice")
    with pytest.raises(ValueError):
        db.add_user("user1", "Bob")

def test_delete_user(db: database):
    db.add_user("user2", "Bob")
    db.delete_user("user2")
    assert db.get_user("user2") is None