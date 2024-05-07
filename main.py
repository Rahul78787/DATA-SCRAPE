from selenium import webdriver
from selenium.webdriver.chrime.service import service
import time

service =Service(executable_path="chromedriver.exe")
driver=webdriverbdriver.Chrome(service=service)
driver.get("https://www.cityofsanrafael.org/major-planning-projects-2/")

time.sleep(10)

driver.quit()