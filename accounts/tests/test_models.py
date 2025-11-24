import pytest
from accounts.models import User


@pytest.fixture
def user():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def superuser():
    return User.objects.create_superuser(username='adminuser', password='adminpassword')

@pytest.mark.django_db
def test_user_create(user):
    assert str(user) == 'testuser'
    assert user.check_password('testpassword')
    assert not user.is_superuser
    assert not user.is_staff


@pytest.mark.django_db
def test_superuser_create(superuser):
    assert str(superuser) == 'adminuser'
    assert superuser.check_password('adminpassword')
    assert superuser.is_superuser
    assert superuser.is_staff