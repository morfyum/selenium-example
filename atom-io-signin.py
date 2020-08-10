from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from time import sleep

# FIREFOX
#browser = webdriver.Firefox(executable_path='./geckodriver')

# CHROME
browser = webdriver.Chrome(executable_path='./chromedriver')

# BROWSER SETTING
browser.set_window_size(1260,700)
browser.set_window_position(10,10)

# BROWSER NAVIGATION
browser.get('https://atom.io/')

# TESTS

# Click to "Sign in"
browser.find_element_by_link_text("Sign in").click()

# write username
input_username = browser.find_element_by_name('login')
input_username.send_keys('asd')

# write password
input_passwd = browser.find_element_by_name('password')
input_passwd.send_keys('12345678')

# try to login
sign_in = browser.find_element_by_name('commit').click()
#sign_in.click()

# Check login result: check exist element
print(browser.find_element_by_class_name("flash-error").text)

sleep(2)

# press browser back button
browser.back()
browser.back()



sleep(5)
browser.quit()
