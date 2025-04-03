from selenium import webdriver

# Setup WebDriver
driver = webdriver.Chrome()

# Open App URL
driver.get("http://myapp.azurewebsites.net")

# Validate Page Title
assert "My App" in driver.title

# Close Browser
driver.quit()
