from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# FIREFOX
#browser = webdriver.Firefox(executable_path='./geckodriver')

# CHROME
browser = webdriver.Chrome(executable_path='./chromedriver')

# BROWSER SETTING
browser.set_window_size(1260,700)
browser.set_window_position(10,10)

# BROWSER NAVIGATION
browser.get('https://hu.wikipedia.org/')

# TESTS

# Test site title
assert 'Wikipédia, a szabad enciklopédia' in browser.title

# find and press button
#button_licence_agree = browser.find_element_by_name('agree')
#button_licence_agree.click()

# FIND IN SEARCH MENU
search_in_wiki = browser.find_element_by_name('search')  # Find the search box
search_in_wiki.send_keys('MTZ-80' + Keys.RETURN)

#elem = browser.find_element_by_name('p')  # Find the search box
#elem.send_keys('seleniumhq' + Keys.RETURN)


# Check with if/else browser title
# select the correct path

print("TITLE: "+browser.title)
if "Keresési eredmények: „MTZ-80” – Wikipédia" == browser.title:
    print("NEED CLICK")
    select_mtz80 = browser.find_element_by_xpath('//*[@title="MTZ-80"]').click()
elif "„MTZ-80” – Wikipédia" == browser.title:
    print("OK")
else:
    print("VALAMI MÁS")
    print("TITLE: "+browser.title)
    exit()

sleep(5)
browser.quit()
