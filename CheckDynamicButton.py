from playwright.sync_api import Page, expect
import pytest

def test_DynamicButton(page: Page):
    page.goto("https://testpages.eviltester.com/challenges/synchronization/dynamic-buttons-01/")

    #Verify Title
    expect(page.locator(".td-content")).to_contain_text("Dynamic Buttons 01")

    #click on Start button
    page.get_by_role("Button", name="start").click()

    #verify One button is visible and waiting for it to be visible
    
    one_button = page.get_by_role("button", name="One")
    one_button.wait_for(state="visible")
    one_button.click()

    #Code to verify Two button
    
    two_button = page.get_by_role("button", name='Two')
    two_button.wait_for(state="visible")
    two_button.click()

    #code for Three button

    three_button = page.get_by_role("button", name='Three')
    three_button.wait_for(state="visible")
    three_button.click()
    
if __name__ == "__main__":
    pytest.main([__file__, "-q"])