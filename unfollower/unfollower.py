################################################################################
# This is a bot that unfollows people, in case you were as sick as me as to
# follow 23256 people. 
# 
# Instructions:
# 1) Install selenium. As always, good luck with that.
# 2) Execute the program (make sure it's past midnight)
# 3) Give it your credentials
################################################################################

from selenium import webdriver
import datetime
import time 

# Prevents the program from running during teaching hours so we do not disturb
# people
# We are going to be using this program during the night from 0h to 8h 
def appropriateTime():
    return datetime.datetime.now().hour > 23 or datetime.datetime.now().hour < 7  

# Login variables. Write here your credentials 
name=input('Username (do not forget the @): ') 
password=input('Password: ')

browser = webdriver.Firefox()
browser.get('https://swad.ugr.es/es')

# Finding the login form  
nameForm = browser.find_element_by_id('UsrId')
passwdForm = browser.find_element_by_id('UsrPwd')
okButton = browser.find_element_by_class_name('BT_SUBMIT.BT_CONFIRM')

# Logging in  
nameForm.send_keys(name)
passwdForm.send_keys(password)
okButton.click()


# May the massive UNfollowing begin
while appropriateTime():
    # Moving to the list of people that you follow 
    myProfile = browser.find_element_by_class_name('HEAD_USR.USR_PURPLE')
    myProfile.click()
    following = browser.find_element_by_xpath('//*[@title="Siguiendo"]')
    following.click()

    # We wait a minute so that the list loads
    time.sleep(60)
    profile = browser.find_element_by_xpath('//*[@title="Dejar de seguir"]')
    profile.click()
    browser.back()
    

print('People are studying >:[ Leave them alone')
