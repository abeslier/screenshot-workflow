import sys, os
from selenium import webdriver


def screenshot(url):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(url)
        driver.save_screenshot("screenshot.png")
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    screenshot(os.path.abspath(sys.argv[1]))
