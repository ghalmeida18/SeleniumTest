from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

driver.get('https://www.magazineluiza.com.br/busca/celulares/?filters=brand---apple')

value1 = driver.find_element(By.XPATH, '//*[@id="__next"]/div/main/section[4]/div[3]/div/ul/li[1]/a/div[3]/div[2]/div/p[2]')

print(value1.text)