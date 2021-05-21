## [ WARNING! ] This *"selenium-example"* documentation is old!

#### AUTHOR:  MÁRTON JÓZSA
#### UPDATE:  2020-08-10

### SYSTEM DEPENDENCIES
```
sudo pip3 install virtualenv
```

### Ceate new selenium env:
```
# Create venv
virtualenv venv

# Activate venv
source venv/bin/activate

# Now you can isnstall dependencies:
pip3 install selenium

# Exit from venv
deactivate
```

### Or restore selenium `venv` from `selenium_env_deplist.list`
```
virtualenv venv

source venv/bin/activate

pip3 install -r selenium_env_deplist.list
```

### Activate `venv` separated environment
```
source venv/bin/activate
```

# SELENIUM BROWSER DRIVERS
https://pypi.org/project/selenium/
  - CHROME:    https://sites.google.com/a/chromium.org/chromedriver/downloads
  - FIREFOX:   https://github.com/mozilla/geckodriver/releases

# SELENIUM DOC / BROWSER MANIPULATION
  - https://www.selenium.dev/documentation/en/webdriver/browser_manipulation/

---
