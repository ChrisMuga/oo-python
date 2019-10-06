from test import addition
from App.Operations.User import User


def test_addition():
    assert addition(3, 2) == 5


def test_user_fetch():
    user = User(name="Test User Onyango", age=26)
    assert len(user.fetch()) >= 0
