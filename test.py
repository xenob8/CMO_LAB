from selenium.webdriver.common.by import By
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path
xpath = '/html/body/div[1]/div[1]/div[2]/div[1]/div/div[2]/div/div[2]/div[1]/div[4]/div[1]/div/div[1]'
driver = webdriver.Chrome()
driver.get("https://magnitcosmetic.ru/catalog/kosmetika/parfyumeriya/muzhskie_aromaty/51664/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    print(element)
    print(element.text)
finally:
    driver.quit()