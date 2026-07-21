from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()

# open website
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# enter username
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# enter password
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# click login
login_button = driver.find_element(By.ID, "login-button")
login_button.click()
time.sleep(2)

# scroll down to product
driver.execute_script("window.scrollBy(0, 300)")
time.sleep(1)

# add to cart
add_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart)
time.sleep(1)
driver.execute_script("arguments[0].click();", add_to_cart)
time.sleep(2)

# open cart
cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
cart_icon.click()
time.sleep(2)

# verify product in cart
product = driver.find_element(By.CLASS_NAME, "inventory_item_name")
print("Product in cart:", product.text)
time.sleep(2)

# click checkout
checkout_button = driver.find_element(By.ID, "checkout")
checkout_button.click()
time.sleep(2)

# enter first name
first_name = driver.find_element(By.ID, "first-name")
first_name.send_keys("Richa")
time.sleep(1)

# enter last name
last_name = driver.find_element(By.ID, "last-name")
last_name.send_keys("Adhikari")
time.sleep(1)

# enter postal code
postal_code = driver.find_element(By.ID, "postal-code")
postal_code.send_keys("12345")
time.sleep(1)

# click continue
continue_button = driver.find_element(By.ID, "continue")
continue_button.click()
time.sleep(2)

# click finish
finish_button = driver.find_element(By.ID, "finish")
driver.execute_script("arguments[0].scrollIntoView(true);", finish_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", finish_button)
time.sleep(2)

# verify order confirmation
confirmation = driver.find_element(By.CLASS_NAME, "complete-header")
print("Order Status:", confirmation.text)
time.sleep(2)

print("Order Placed Successfully!")

# click back home
back_button = driver.find_element(By.ID, "back-to-products")
driver.execute_script("arguments[0].scrollIntoView(true);", back_button)
time.sleep(1)
driver.execute_script("arguments[0].click();", back_button)
time.sleep(2)

print("Back to Home Page!")

driver.quit()