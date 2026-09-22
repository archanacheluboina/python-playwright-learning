from playwright.sync_api import Page, expect
import pytest

def test_waiting_for_Elements(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    #Added Explicit Wait
    page.locator(".title").wait_for(state="visible")

    expect(page.locator(".title")).to_contain_text("Products")

if __name__ == "__main__":
    pytest.main([__file__, "-q"])