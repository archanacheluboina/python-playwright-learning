from playwright.sync_api import Page, expect
import pytest

def test_dropdownSelection(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(3000)

    #verify the URL
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    #Select the value from dropdown
    page.get_by_label("Sort products").select_option("lohi")

    #Verify that it value appears as selected in drop down
    expect(page.get_by_label("Sort products")).to_have_value("lohi")

    #verify that the lowest-priced item appears first
    expect(page.locator(".inventory_item_price").first).to_have_text("$7.99")
    page.wait_for_timeout(3000)
    
    #Change the drop down value
    page.get_by_label("Sort products").select_option("za")

    #Verify that it value appears as selected in drop down
    expect(page.get_by_label("Sort products")).to_have_value("za")

    #Verify that the Item appears as first after sorting
    expect(page.locator(".inventory_item_name").first).to_have_text("Test.allTheThings() T-Shirt (Red)")

    page.wait_for_timeout(3000)
    
if __name__ == "__main__":
    pytest.main([__file__, "-q"])
    