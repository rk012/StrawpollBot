from selenium import webdriver

TOR_BINARY = ""  # path to tor executable

POLL_ID = 45483463  # strawpoll.me/<id>
CHOICE = "A"
VOTE_COUNT = 10

HEADLESS = True  # Set this to false to enable window visibility while submitting votes


# get a new selenium webdriver with tor as the proxy
def get_tor_instance():
    options = webdriver.FirefoxOptions()
    options.binary_location = TOR_BINARY
    options.headless = HEADLESS

    return webdriver.Firefox(options=options)


for i in range(1, VOTE_COUNT + 1):
    driver = get_tor_instance()

    # noinspection PyBroadException
    try:
        driver.get(f"https://www.strawpoll.me/{POLL_ID}")
        driver.find_element_by_id(f"field-options-{CHOICE.lower()}").click()  # Select choice
        driver.find_element_by_css_selector(".poll > footer:nth-child(6) > button:nth-child(1)").click()  # Submit
        print(f"Submited vote {i}")
        driver.close()
    except KeyboardInterrupt:
        driver.quit()
        break
    except Exception:
        print(f"Unable to submit vote {i}")
        driver.close()
