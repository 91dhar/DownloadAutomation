import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# refer https://pypi.org/project/webdriver-manager/
from webdriver_manager.chrome import ChromeDriverManager

os.environ['PATH'] += r"C:/SeleniumDriver"
options = webdriver.ChromeOptions()  # Added with research
options.add_experimental_option("detach", True)  # Added with research
driver = webdriver.Chrome(
    options=options, service=Service(ChromeDriverManager().install()))  # Options added post research. Need more research.
# URL is of the download button.
driver.get('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86')
driver.maximize_window()
my_element = driver.find_element("id", "downloadButton")
my_element.click()
