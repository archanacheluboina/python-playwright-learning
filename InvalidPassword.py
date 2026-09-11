from playwright.sync_api import Page, expect
import pytest

def test_invalidpassword (page: Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrongpassword")
    page.get_by_role("button", name="Login").click()

    #verify the url after incorrect password
    expect(page).to_have_url("https://www.saucedemo.com/")

    #verify error message
    expect(page.get_by_role("alert")).to_have_text(
    "Epic sadface: Username and password do not match any user in this service"
)

if __name__ == "__main__":
	pytest.main([__file__, "-q"])