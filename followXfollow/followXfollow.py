################################################################################################################
# OVERVIEW
# This is a web scrapper for gaining followers on SWAD
# It works by following random people and specting them to follow you back
#
# USAGE INSTRUCTIONS
# 1) Install selenium. Good luck with that.
# 2) Run the program
# 3) Give it your credentials 
################################################################################################################

from selenium import webdriver
import datetime

# Prevents the program from running during teaching hours so we do not disturb people
# We are going to be using this program during the night from 0h to 8h 
def appropriateTime():
    return datetime.datetime.now().hour > 23 or datetime.datetime.now().hour < 8  

# Login variables. Write here your credentials 
name=input('Name (do not forget the @):' ) 
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

# May the massive following begin
while appropriateTime():
    # Moving to Start->Profiles
    start = browser.find_element_by_xpath('//*[@title="Inicio"]')
    start.click()
    startProfiles = browser.find_element_by_xpath('//*[@title="Perfiles públicos de usuarios"]')
    startProfiles.click()

    # Following every person 
    profile = browser.find_element_by_xpath('//*[@title="Seguir"]')
    profile.click()
    browser.back()

print('People are studying >:[ Leave them alone')
    
    
