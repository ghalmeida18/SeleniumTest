from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()

driver.get('https://www.kohls.com/catalog/mens-nike-shoes.jsp?CN=Gender:Mens+Brand:Nike+Department:Shoes&icid=sl-nav-ftw-shoes-mens-nike&kls_sbp=84311432945461347682116220168293182461')

value1 = driver.find_element(By.XPATH, '//*[@id="902047_prod_price"]/div[1]/span[1]')

value2 = driver.find_element(By.XPATH, '//*[@id="5013248_prod_price"]/div[1]/span[1]')

print(f'The product 1 has value: {value1.text}. The product 2 has value: {value2.text}')

