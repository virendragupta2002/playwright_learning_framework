from playwright.sync_api import Playwright, Page, expect

def test_saved_loginstate(page:Page):
    context = page.context.browser.new_context(storage_state="state.json")
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client/#/dashboard/dash")
    expect(page.get_by_role("button", name="ORDERS")).to_be_visible()
