import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


browser = webdriver.Chrome()

category = raw_input("Enter a Category ")

item = raw_input("Enter the keyword of the item you want you would want... ")

anything = raw_input("Welcome to Supreme Bot made by @ijh_0 ... Hit anything and Enter to begin...")

browser.get("https://www.supremenewyork.com/shop/all/" + category)

element = browser.find_elements_by_partial_link_text(item)

for i in range(len(element)):

	element = browser.find_elements_by_partial_link_text(item)
	element[i].click()
	i = 0
	while True:
		try:
			if (i > 75):
				break
			soldOut = browser.find_element_by_xpath("/html[@class=' js no-touch csstransforms']/body[@class=' products show us']/div[@id='wrap']/div[@id='container']/div[@id='details']/div[@id='cctrl']/form/fieldset[@id='add-remove-buttons']/b[@class='button sold-out']")
			print "trying"
			if soldOut.is_displayed():
				browser.back()	
#			wait = WebDriverWait(browser, 15)
#			addcartLoop = wait.until(EC.element_to_be_clickable((By.NAME,'commit')))
#			if addCartLoop.is_displayed():
#				j = False
#				break


		except NoSuchElementException:
			i = i + 1
			print i
			continue
		break
	if (i > 75):
		break

wait = WebDriverWait(browser, 15)
addcart = wait.until(EC.element_to_be_clickable((By.NAME,'commit')))

addcart.click()

checkout = WebDriverWait(browser, 10).until(EC.element_to_be_clickable(
	(By.XPATH, "/html[@class=' js no-touch csstransforms']/body[@class=' products show us']/div[@id='wrap']/div[@id='container']/div[@class='sidebar']/div[@id='cart']/a[@class='button checkout']")))


checkout.click()

name = 'Dummy Name'
email = 'trippin@gmail.com'
tel1 = '1234567890'
address = 'Dont Trip St.'
secondaddress = 'example'
zipcode = '93117'
city = 'Goleta'

ccnumber = '1234123512361237'
ccmonth = '11'
ccyear = '2019'

cvv = '123'

# Name
input_name = browser.find_element_by_id('order_billing_name')
input_name.send_keys(name)

# Email
input_email = browser.find_element_by_id('order_email')
input_email.send_keys(email)

# Telephone
input_telephonept1 = browser.find_element_by_id('order_tel')
input_telephonept1.clear()
input_telephonept1.send_keys(tel1)


# Address 
input_address = browser.find_element_by_id('bo')
input_address.send_keys(address)

# 2nd Address
#input_2ndaddress = browser.find_element_by_id('oba3')
#input_2ndaddress.send_keys(secondaddress)

# Zip Code
input_zip = browser.find_element_by_id('order_billing_zip')
input_zip.send_keys(zipcode)

# State
input_state = browser.find_element_by_id('order_billing_state')
input_state.send_keys('CA')

# Credit card
input_credit = browser.find_element_by_id('cnb')
input_credit.clear()
input_credit.send_keys(ccnumber)

# Credit Card Month
input_ccmonth = browser.find_element_by_id('credit_card_month')
input_ccmonth.send_keys(ccmonth)

# Credit Card Year
input_ccyear = browser.find_element_by_id('credit_card_year')
input_ccyear.send_keys(ccyear)

# CVV
input_cvv = browser.find_element_by_id('vval')
input_cvv.send_keys(cvv)

# Order Terms
wait = WebDriverWait(browser, 15)
terms = wait.until(EC.element_to_be_clickable((By.XPATH, "/html[@class=' js no-touch csstransforms']/body[@class=' cart checkout_page us']/div[@id='wrap']/div[@id='content']/form[@id='checkout_form']/div[@id='cart-body']/div[@id='cart-cc']/fieldset/p[2]/label[@class='has-checkbox terms']")))
terms.click()

# Checkout time!
wait = WebDriverWait(browser, 15)
officialCheckout = wait.until(EC.element_to_be_clickable((By.NAME,'commit')))

officialCheckout.click()














