import json

from selenium import webdriver

TOR_BINARY = ""  # path to tor executable


# get a new selenium webdriver with tor as the proxy
def get_tor_instance():
    options = webdriver.FirefoxOptions()
    options.binary_location = TOR_BINARY

    return webdriver.Firefox(options=options)


while True:
    driver = get_tor_instance()
    try:
        driver.get("view-source:https://httpbin.org/ip")
        print(json.loads(driver.find_element_by_tag_name("pre").text)["origin"], end="")
        input()
        driver.close()
    except KeyboardInterrupt:
        driver.quit()
        break
