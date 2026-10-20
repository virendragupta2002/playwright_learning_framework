
from playwright.sync_api import Page, Route

def intercept_request(route: Route):
    headers = route.request.headers.copy()   # start from the real headers
    headers["x-custom-header"] = "test-value"    #mocking data
    route.continue_(headers=headers)

    

def test_networkInterceptRequest(page: Page):
    
    page.route("https://demo.playwright.dev/api-mocking/api/v1/fruits", intercept_request)
    page.goto("https://demo.playwright.dev/api-mocking/")
    page.pause()

