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

	# Adding Bike & Sauce Labs Backpack to cart from inventory page
	page.locator(".inventory_item").filter(
		has_text="Sauce Labs Bike Light"
	).get_by_role("button", name="Add to cart").click()

	# Adding Sauce Labs Backpack to cart from inventory page
	page.locator(".inventory_item").filter(
		has_text="Sauce Labs Backpack"
	).get_by_role("button", name="Add to cart").click()

	#Adding Sauce Labs Bolt T-Shirt to cart from inventory page
	page.locator(".inventory_item").filter(has_text="Sauce Labs Bolt T-Shirt"
	).get_by_role("button", name="Add to cart").click()


	#Checking the shopping cart badge displays 3
	expect(page.locator(".shopping_cart_badge")).to_have_text("3")

	#Click on the shopping cart link to go to the cart page
	page.locator(".shopping_cart_link").click()

	#verifying the url of the page is correct
	expect(page).to_have_url("https://www.saucedemo.com/cart.html")

	# Verify total items added
	expect(page.locator(".cart_item")).to_have_count(3)

	page.wait_for_timeout(3000)

if __name__ == "__main__":
	pytest.main([__file__, "-q"])