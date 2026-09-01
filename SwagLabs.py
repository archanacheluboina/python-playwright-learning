from playwright.sync_api import Page, expect
import pytest


def test_saucedemo_login(page: Page):
	page.goto("https://www.saucedemo.com/")
	page.get_by_placeholder("Username").fill("standard_user")
	page.get_by_placeholder("Password").fill("secret_sauce")
	page.get_by_role("button", name="Login").click()
	page.wait_for_timeout(3000)

	# Verify successfull login
	expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

	# Adding Bike to cart
	page.get_by_text("Sauce Labs Bike Light").click()
	expect(page).to_have_url("https://www.saucedemo.com/inventory-item.html?id=0")
	expect(page.get_by_text("Sauce Labs Bike Light")).to_be_visible()
	page.get_by_role("button", name="Add to cart").click()
	page.locator(".shopping_cart_link").click()

	#check the url of shoping cart page
	expect(page).to_have_url("https://www.saucedemo.com/cart.html")

	# Verify item is added to cart
	expect(page.get_by_role("link", name="Sauce Labs Bike Light")).to_be_visible()

	print("Assertion Tested and Locators by placeholder and role are working fine")
	print("Test Passed - Bike Light successfully added to cart")
	page.wait_for_timeout(3000)

if __name__ == "__main__":
	pytest.main([__file__, "-q"])