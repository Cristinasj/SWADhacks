#########################################################################
# Creator: cristinasj
# Follow me on SWAD :D 
#
# INSTRUCTIONS:
# 1) Go to Communication -> Messages
# 2) Write a message but don't send it 
# 3) Execute this program in another window
# 4) In case of loosing control, move the cursor to the
#    top left corner of the window or press cntrl C
# 5) If you have two monitors, the program will be executed
#    in the left monitor
##########################################################################

import pyautogui
import time 

# This variables are a safety mechanism
pyautogui.PAUSE = 3
pyautogui.FAILSAFE = True

# Variables for the program 
Send = (958,382)
Scrolls=-999
Back = (85, 84)


# Scroll
pyautogui.moveTo(Send)
pyautogui.scroll(Scrolls)


# Here's where the loop starts 
while (True):

    # Send the message
    pyautogui.click(Send)

    # go back
    pyautogui.click(Back)

    # Waits a min just in case SWAD thinks we're a robot
    #time.sleep(10)
