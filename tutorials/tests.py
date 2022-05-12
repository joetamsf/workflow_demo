from django.test import TestCase
from django.urls import reverse
from tutorials.models import Tutorial
import pytest

def test_homepage_access():
    url = reverse('home')
    assert url == '/'

# @pytest.mark.django_db
# def test_create_tutorial(tutorial):
#     tutorial = Tutorial.objects.create(
#         title='Pytest',
#         tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
#         description='Tutorial on how to apply pytest to a django application',
#         published=True
#     )
#     assert tutorial.title == "Pytest"

@pytest.mark.django_db
def test_create_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == "Pytest"

@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://someurl',
        description='Tutorial111',
        published=True
    )
    return tutorial

@pytest.fixture
def test_user(db, django_user_model):
    django_user_model.objects.create_user(
        username="test_username", password="test_password")
    return "test_username", "test_password"

def test_login_user(client, test_user):
    test_username, test_password = test_user
    login_result = client.login(username=test_username, password=test_password)
    assert login_result == True


def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()

def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()



# Create your tests here.
