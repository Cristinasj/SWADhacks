##############################################################################
#
# This unfollower is 6 times faster than the previous version, unfollowing
# the unbelieveble amount of 2 (TWO!) people per minute.
#
# In my defense, following people is ridiculously much faster than unfollowing
# them because their profile page has to load.
#
##############################################################################

from selenium import webdriver
import time 
name=input('Name: ')
password=password('Password: ')
browser = webdriver.Firefox()
browser.get('https://swad.ugr.es/es')
nameForm = browser.find_element_by_id('UsrId')
passwdForm = browser.find_element_by_id('UsrPwd')
okButton = browser.find_element_by_class_name('BT_SUBMIT.BT_CONFIRM')
nameForm.send_keys(name)
passwdForm.send_keys(password)
okButton.click()
myProfile = browser.find_element_by_class_name('HEAD_USR.USR_PURPLE')
myProfile.click()
following = browser.find_element_by_xpath('//*[@title="Siguiendo"]')
following.click()
time.sleep(90)
profiles = browser.find_elements_by_xpath('//*[@title="Dejar de seguir"]')
for p in range(len(profiles)):
    profiles[p].click()
    browser.back()
    profiles = browser.find_elements_by_xpath('//*[@title="Dejar de seguir"]')
