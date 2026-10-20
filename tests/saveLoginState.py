from playwright.sync_api import Playwright, Page, expect

def test_saveLogin(page:Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("vgvirendra@gmail.com")
    page.get_by_placeholder("enter your passsword").fill("Veeru@2026")
    page.get_by_role("button", name="Login").click()

    # IMPORTANT: wait until login is really complete before saving
    page.wait_for_load_state("networkidle")
    expect(page.get_by_role("button", name="ORDERS")).to_be_visible()

    page.context.storage_state(path="state.json")   # save AFTER login completes