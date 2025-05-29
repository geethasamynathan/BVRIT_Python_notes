import pytest
from demo3 import Database

@pytest.fixture
def db():
    """Creates a fresh instance of Database before each test."""
    database= Database()
    yield database # proveide the fixture instance
    database.data.clear()  # Clear the database after tests
    
def test_add_user(db):
    db.add_user("1", "Geetha")
    assert db.get_user("1") == "Geetha"
    
def test_add_duplicate_user(db):
    db.add_user("1", "Geetha")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user("1", "Geetha")  # Attempt to add duplicate user    
        
def test_delete_user(db):
    db.add_user("2", "sample")
    db.delete_user("2")
    assert db.get_user("2") is None  # User should be deleted
    
    