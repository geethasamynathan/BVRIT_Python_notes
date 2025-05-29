import pytest
from demo2 import UserManager
# @pytest.fixture
# def user_manager():
#     "creates fresh instance of UserManager before each test."
#     return UserManager()

user_manager = UserManager() #instance of UserManager
def test_add_user():
    assert user_manager.add_user("geetha", "geetha@mail.com") == True
    assert user_manager.get_user("geetha") == "geetha@mail.com"
    
def test_add_duplicate_user():
    user_manager.add_user("geetha", "geetha@mail.com")  
    with pytest.raises(ValueError):
        user_manager.add_user("geetha", "geetham@mail.com")  