import time, json, pytest
from playwright.sync_api import Playwright, Page, expect
from utils.apiFrameworkUtils import apiBase
from pageObjects.loginPage import LoginPage
from pageObjects.dashboard import DashboardPage
from pageObjects.orderhistory import OrderHistoryPage

with open('testdata/credentials.json') as f:
        test_data=json.load(f)
        ##print(test_data)
        user_credentials_list = test_data['user_credentials']
        ##print(user_credentials_list)

@pytest.mark.smoke
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_eComPractice(playwright: Playwright, browserInstance, user_credentials):
        email = user_credentials["userEmail"]
        password = user_credentials["userPassword"]
        
        apiutil_obj = apiBase()            ##create object of apiBase class
        orderId = apiutil_obj.createOrder(playwright, user_credentials)  

        #Login Page
        loginPage = LoginPage(browserInstance)
        loginPage.navigate()
        dashboard = loginPage.login(email,password)       #Dashboard Page
        
        orderHistory = dashboard.navigateToOrders(orderId)       #OrderHistory
        
        orderHistory.viewOrders(orderId)






       