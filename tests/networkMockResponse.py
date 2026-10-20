from playwright.sync_api import Playwright, Page, expect, Route
import time

def intercept_response(route: Route):                     # real call, real headers
    route.fulfill(json={"tags": ["Kiko", "Veer", "Testing"]})

def test_networkMock_response(page: Page):
    # page.goto("https://rahulshettyacademy.com/client")
    # page.get_by_placeholder("email@example.com").fill("vgvirendra@gmail.com")
    # page.get_by_placeholder("enter your passsword").fill("Veeru@2026")
    # page.get_by_role("button", name="Login").click()
    # page.route("**/get-orders-for-customer", intercept_response)
    # page.get_by_role("button", name="ORDERS").click()
    # order_text=page.locator(".mt-4").text_content()
    # print(order_text)

    page.route("**/api/tags*", intercept_response)
    page.goto("https://conduit.bondaracademy.com/")
    expect(page.get_by_text("Kiko")).to_be_visible()