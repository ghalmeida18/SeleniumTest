from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import csv

driver = Chrome()

driver.get('https://www.kohls.com/catalog/mens-nike-shoes.jsp?CN=Gender:Mens+Brand:'
           'Nike+Department:Shoes&icid=sl-nav-ftw-shoes-mens-nike&kls_sbp=84311432945461347682116220168293182461')

value1 = driver.find_element(By.XPATH, '//*[@id="902047_prod_price"]/div[1]/span[1]')

value2 = driver.find_element(By.XPATH, '//*[@id="4228758_prod_price"]/div[1]/span[1]')

print(f'The product 1 has value: {value1.text}. The product 2 has value: {value2.text}')

#CSV

with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(("Value1", "Value2"))
    writer.writerow((value1.text, value2.text))
