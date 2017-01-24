from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/home/usr/programs/anaconda3/geckodriver')
driver.get('http://www.autotrader.ca/a/Mercedes-Benz/NAVION/LONGUEUIL/Quebec/19_9893995_/?ms=rv&ursrc=pl&urp=3&urm=8&showcpo=ShowCPO')
time.sleep(3)
driver.execute_script("$('.phoneNumberHolder div[id$=MaskablePhoneNumberButton]').click();")
print(driver.find_element_by_class_name("lblPhone").text)
driver.close()