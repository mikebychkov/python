from playwright.sync_api import sync_playwright

# Input data
data = {
    "name": "some name",
    "birthdate": "2000-01-01",
    "sex": "Male"
}

# Target URL
url = "https://example.com/form"  # Replace with your real form URL

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    
    page.goto(url)

    # Fill inputs by their name attributes
    page.fill('input[name="person_name"]', data["name"])
    page.fill('input[name="p_birthdate"]', data["birthdate"])
    page.fill('input[name="sex_of_person"]', data["sex"])

    # Optionally click submit if needed
    # page.click('button[type="submit"]')

    # For debug: take a screenshot to verify it's filled correctly
    page.screenshot(path="filled_form.png")

    browser.close()
