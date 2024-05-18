# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# # Configure the remote WebDriver using Selenium Grid
# capabilities = DesiredCapabilities.FIREFOX.copy()
# capabilities['browserName'] = 'firefox'

# # Replace 'localhost:4444' with the actual address of your Selenium Grid hub
# grid_url = 'http://localhost:4444/wd/hub'

# # Create a remote WebDriver instance pointing to the Selenium Grid hub
# try:
#     driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)
# except Exception as e:
#     print("Error submitting form: ", e)

# # Open the Python website
# driver.get('http://www.python.org')

# # Perform any further actions as needed...
# print("The test was done successfully")

# # Close the browser
# driver.quit()

# from selenium import webdriver

# # Create a remote WebDriver instance pointing to the Selenium Grid hub
# try:
#     driver = webdriver.Remote(
#         command_executor='http://127.0.0.1:4444/wd/hub',
#         desired_capabilities={'browserName': 'firefox', 'javascriptEnabled': True}
#         )
# except Exception as e:
#     print("Error submitting form: ", e)

# # Open the Python website
# driver.get('http://www.python.org')

# # Perform any further actions as needed...
# print("The test was done successfully")

# # Close the browser
# driver.quit()


from selenium import webdriver
from selenium.webdriver.firefox.options import Options

try:
    options = Options()
    options.add_argument("--javascriptEnabled")
    driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4444/wd/hub',
        options=options
    )
except Exception as e:
    print("Error submitting form:", e)

driver.get('http://www.python.org')

print("The test was done successfully")

driver.quit()
