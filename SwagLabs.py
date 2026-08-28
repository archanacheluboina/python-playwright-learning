from playwright.sync_api import Page, expect
import pytest


def test_saucedemo_login(page: Page):
	page.goto("https://www.saucedemo.com/")
	page.get_by_placeholder("Username").fill("standard_user")
	page.get_by_placeholder("Password").fill("secret_sauce")
	page.get_by_role("button", name="Login").click()
	page.wait_for_timeout(3000)

	expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
	expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
	print("Assertion Tested and Locators by placeholder and role are working fine")
	page.wait_for_timeout(3000)

if __name__ == "__main__":
	pytest.main([__file__, "-q"])