from playwright.sync_api import sync_playwright
import random
import time

# Input data
data = {
    "name": "some name",
    "birthdate": "2000-01-01",
    "sex": "Male"
}

# Target URL
url = "https://example.com/form"  # Replace with actual page

def simulate_human_typing(page, selector, text, delay_range=(0.05, 0.15)):
    for char in text:
        page.locator(selector).type(char, delay=random.uniform(*delay_range))

with sync_playwright() as p:
    # Use a real device profile
    device = p.devices['Pixel 5']  # Or 'iPhone 12', etc.

    browser = p.chromium.launch(headless=False)  # headless=False helps bypass detection
    context = browser.new_context(
        **device,
        locale="en-US",
        user_agent="Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/114.0.5735.131 Mobile Safari/537.36",
        viewport={'width': 393, 'height': 851},  # Mobile screen
        java_script_enabled=True
    )

    # Modify navigator.webdriver to prevent detection
    context.add_init_script("""Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""")

    page = context.new_page()
    page.goto(url, timeout=60000)

    # Wait until form is visible
    page.wait_for_selector('input[name="person_name"]', timeout=10000)

    # Simulate human typing
    simulate_human_typing(page, 'input[name="person_name"]', data["name"])
    simulate_human_typing(page, 'input[name="p_birthdate"]', data["birthdate"])
    simulate_human_typing(page, 'input[name="sex_of_person"]', data["sex"])

    # Wait a bit to simulate user pause
    time.sleep(random.uniform(1, 2))

    # Take a screenshot for verification
    page.screenshot(path="realistic_filled_form.png")

    # Optionally submit form
    # page.click('button[type="submit"]')

    browser.close()
