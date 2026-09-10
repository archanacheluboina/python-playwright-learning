from playwright.sync_api import Page, expect
import pytest

def test_checkout_form_automation(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(3000)

    #verify successfull login
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    #Adding items to cart from inventory page
    page.locator(".inventory_item").filter(has_text="Sauce Labs Onesie").get_by_role("button", name="Add to cart").click()
    page.locator(".inventory_item").filter(has_text="Test.allTheThings() T-Shirt (Red)").get_by_role("button", name="Add to cart").click()

    #verify the badge count of items in the cart
    expect(page.locator(".shopping_cart_badge")).to_have_text("2")  

    #Click on the shopping cart link to go to the cart page
    page.locator(".shopping_cart_link").click()

    page.wait_for_timeout(3000)

    #click on checkout button to go to checkout page
    page.get_by_role("button", name="Checkout").click()

    #verify the url of the page is correct
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")

    page.get_by_placeholder("First Name").fill("Archana")
    page.get_by_placeholder("Last Name").fill("Cheluboina")
    page.get_by_placeholder("Zip/Postal Code").fill("500032")

    #verify that the values are entered in textboxes
    expect(page.get_by_placeholder("First Name")).to_have_value("Archana")
    expect(page.get_by_placeholder("Last Name")).to_have_value("Cheluboina")
    expect(page.get_by_placeholder("Zip/Postal Code")).to_have_value("500032")

    #click on continue button
    page.get_by_role("button", name="Continue").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")

    #verify Payment Information
    expect(page.locator(".summary_info")).to_contain_text("Payment Information:")
    expect(page.locator(".summary_info")).to_contain_text("SauceCard #")
    expect(page.locator(".cart_item").filter(has_text="Sauce Labs Onesie")).to_contain_text("Sauce Labs Onesie")
    expect(page.locator(".cart_item").filter(has_text="Test.allTheThings() T-Shirt (Red)")).to_contain_text("Test.allTheThings() T-Shirt (Red)")

    #Verify Finish button is visible
    expect(page.get_by_role("button", name="Finish")).to_be_visible()
    
    # verify Finish button is visible
    expect(page.get_by_role("button", name="Finish")).to_be_visible()

    # Click on Finish button
    page.get_by_role("button", name="Finish").click()

    #verify the url of the page is correct
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")

    #verify the order confirmation message
    expect(page.locator(".complete-header")).to_have_text("Thank you for your order!")

    page.wait_for_timeout(3000)
    
if __name__ == "__main__":
    pytest.main([__file__, "-q"])