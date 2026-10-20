from playwright.sync_api import Playwright
##loginCredential = {"userEmail": "vgvirendra@gmail.com", "userPassword": "Veeru@2026"}
orderDetails = {"orders": [{"country": "India", "productOrderedId": "6960eae1c941646b7a8b3ed3"}]}

class apiBase:

    def getToken(self, playwright:Playwright, user_credentials):
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/auth/login",
                                    data=user_credentials)
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def createOrder(self, playwright:Playwright, user_credentials):
        token = self.getToken(playwright, user_credentials)
        api_request = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request.post("/api/ecom/order/create-order",
                                    data=orderDetails,
                                    headers={"Authorization": token, "content-type": "application/json"
                                    })
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][0]
        return orderId
        
