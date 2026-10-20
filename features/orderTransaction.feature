Feature: Order transaction verification
    Tests related to Order transaction

    Scenario Outline: Verify the order successfully displayed
        Given place the order with <username> and <password> and get the orderID
        And navigate to home page
        When click the Orders page and all the orders display
        And go to view order and check message displayed
        Then Verify order successfully placed message is displayed 
        Examples:
        | username             | password   |
        | vgvirendra@gmail.com | Veeru@2026 |



