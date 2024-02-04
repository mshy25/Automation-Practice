from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Fix the import statement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cooky_id="bigCookie"
cookies_id="cookies"
product_prefix="product"
product_price_prefix="productPrice"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()


cooky=driver.find_element(By.ID,cooky_id)

while True:
    cooky.click()
    cooky_count=driver.find_element(By.ID,cookies_id).text.split(" ")[0]
    cookies_count=int(cooky_count.replace(",",""))
    print(cooky_count)

    for i in range(4):
        product_price=driver.find_element(By.ID,product_price_prefix+str(i)).text.replace(",","")

        if not  product_price.isdigit():
            continue

        product_price= int(product_price)

        if  cookies_count >=  product_price:
            product=driver.find_element(By.ID,product_prefix+str(i))
            product.click()
            break


time.sleep(10)