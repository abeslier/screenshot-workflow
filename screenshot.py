import sys, os
from selenium import webdriver


def screenshot(input_path, output_path):
    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    try:
        driver.get(input_path)
        driver.save_screenshot(output_path)
    except Exception as e:
        print(e)
    finally:
        driver.quit()


if __name__ == "__main__":
    screenshot(f"file:///{os.path.abspath(sys.argv[1])}", sys.argv[2])
