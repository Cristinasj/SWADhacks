#########################################################################
# Creator: cristinasj
# Follow me on SWAD :D 
#
# INSTRUCTIONS:
# 1) Go to Communication -> Messages
# 2) Make sure the last message you've received is opened
# 3) Execute this program in another window
# 4) In case of loosing control, move the cursor to the
#    top left corner of the window
# 5) If you have two monitors, the program will be executed
#    in the left monitor
##########################################################################

import pyautogui
import time 

# This variables are a safety mechanism
pyautogui.PAUSE = 1.5
pyautogui.FAILSAFE = True

# Variables for the program 
width, height = pyautogui.size()
Answer = (329, 987)
Text = (840, 719)
Message = 'Mensaje automatico. Si es mi profe de AC lamento las molestias'
Send = (958,382)
Scrolls=-999
Back = (85, 84)

# Click answer
pyautogui.click(Answer)

# Put the cursor in the text box
pyautogui.click(Text)

# Write the message
pyautogui.typewrite(Message)


# Scroll
pyautogui.scroll(Scrolls)

# Here's where the loop starts 
while (True): 

    # Send the message
    pyautogui.click(Send)

    # go back
    pyautogui.click(Back)

    # Waits a min just in case SWAD thinks we're a robot
    time.sleep(10)
