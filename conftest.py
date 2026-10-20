import pytest
from playwright.sync_api import Page

@pytest.fixture(scope='session')
def user_credentials(request):
    return request.param

@pytest.fixture
def browserInstance(page: Page):
    return page
