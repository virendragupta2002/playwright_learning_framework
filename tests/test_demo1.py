import time, pytest
from playwright.sync_api import Playwright, Page, expect
from utils.apiUtils import apiBase

# def test_firefoxBrowser(playwright: Playwright):
#    firefoxPage = playwright.firefox.launch().new_page()
#    #page = firefoxBrowser.new_page()
#    firefoxPage.goto("https://rahulshettyacademy.com/client")

@pytest.mark.smoke
def test_eComPractice(playwright: Playwright):  
        browser = playwright.chromium.launch(headless=False)
        chromePage = browser.new_context().new_page()

        apiutil_obj = apiBase()                                 ##create object of apiBase class
        orderId = apiutil_obj.createOrder(playwright)           #call method of apiBase 

        #Login
        chromePage.goto("https://rahulshettyacademy.com/client")
        chromePage.get_by_placeholder("email@example.com").fill("vgvirendra@gmail.com")
        chromePage.get_by_placeholder("enter your passsword").fill("Veeru@2026")
        chromePage.get_by_role("button", name="Login").click()

        #OrderHistoryPage Verify
        chromePage.get_by_role("button", name="ORDERS").click()
        expect(chromePage.get_by_role("table")).to_contain_text(orderId)
        orderTable = chromePage.get_by_role("table")
        orderTable.get_by_role("button", name="View").first.click()  ##we can use nth(0) also in place of first
        expect(chromePage.get_by_text(orderId)).to_be_visible()


def test_automationDemo(page:Page):
    api_util_obj = apiUtils()
    api_util_obj.createOrder()
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("vgvirendra@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Veeru@2026")
    page.get_by_role("button", name="Login").click()
    # page.locator(".blinkingText").click()
    # expect(page.get_by_text("Incorrect email or password")).to_be_visible();
    product = page.locator("#products").filter(has_text="ZARA COAT 3")
    print(product)
    page.hover
    # Handle child window
    with page.expect_popup() as newPageInfo:
         page.get_by_role("link", name="Explore the QA Career Accelerator", exact=False).click()
         childPage = newPageInfo.value
         childPage.wait_for_load_state()
         expect(childPage).to_have_url("https://rahulshettyacademy.com/qa-career-accelerator-job-ready")