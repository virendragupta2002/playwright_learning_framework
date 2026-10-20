import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from utils.apiFrameworkUtils import apiBase
from pageObjects.loginPage import LoginPage
from pageObjects.dashboard import DashboardPage
from pageObjects.orderhistory import OrderHistoryPage

scenarios('./features/orderTransaction.feature')

@pytest.fixture
def shared_data():
    return {}

@given(parsers.parse('place the order with {username} and {password} and get the orderID'))
def place_order(playwright, username, password):
    user_credentials= {"username": "vgvirendra@gmail.com", "password": "Veeru@2026"}
    apiutil_obj = apiBase()            
    orderId = apiutil_obj.createOrder(playwright, user_credentials)
    shared_data['order_id'] = orderId

def login(browserInstance,shared_data):
    loginPage = LoginPage(browserInstance)
    loginPage.navigate()
    shared_data['login_page'] = loginPage

@when('click the Orders page and check all the orders display')
def Orders_page(username, password, shared_data):
    loginPage = shared_data['login_page']
    dashboard = loginPage.login(username,password)
    shared_data['dashboard_page'] = dashboard

@when('go to view order and check message displayed')
def click_viewOrder(shared_data):
    dashboard = shared_data['dashboard_page']
    orderId = shared_data['order_id']
    orderHistory = dashboard.navigateToOrders(orderId)
    shared_data['order_history'] = orderHistory

@then('Verify order successfully placed message is displayed')
def verify_message(shared_data):
    orderId = shared_data['order_id']
    orderHistory = shared_data['order_history']
    orderHistory.viewOrders(orderId)
