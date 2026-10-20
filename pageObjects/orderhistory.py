from playwright.sync_api import expect

class OrderHistoryPage:

    def __init__(self, page):
        self.page = page

    def viewOrders(self, orderId):
        orderTable = self.page.get_by_role("table")
        orderTable.get_by_role("button", name="View").first.click()      ##we can use nth(0) also in place of first
        expect(self.page.get_by_text(orderId)).to_be_visible()

    