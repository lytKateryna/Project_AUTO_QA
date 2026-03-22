from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pytest
# import os

header_text = driver.find_element(By.TAG_NAME, "h4")
print(header_text.text)

