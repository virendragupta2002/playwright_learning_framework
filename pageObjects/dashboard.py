import re
from .orderhistory import OrderHistoryPage
from playwright.sync_api import expect

class DashboardPage:

    def __init__(self,page):
        self.page = page

    def navigateToOrders(self, orderId):
        self.page.get_by_role("button", name="ORDERS").click()
        expect(self.page.get_by_role("table")).to_contain_text(orderId)
        orderHistory = OrderHistoryPage(self.page)
        return orderHistory


