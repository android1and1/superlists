# not run this in acturely server! it is for client(installed python3 and selenium)
from selenium import webdriver 
browser = webdriver.Firefox()
browser.get('http://54.199.137.210')
assert 'Django' in browser.title
