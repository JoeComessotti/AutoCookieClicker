# This project uses the selenium module, the time module and the tkinter module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common import exceptions
import time
from tkinter import *

# Class for the auto clicker
# init function creates a variable for the webdriver  
class AutoClicker():
    def __init__(self):
        self.bot = webdriver.Chrome()

    # Go function makes the webdriver:
    # 1. Open Chrome and go to the url for cookie clicker
    def go(self, save, run):
        bot = self.bot
        bot.get('https://orteil.dashnet.org/cookieclicker/')
        time.sleep(3)
        
    # 2. If the save code variable passed as a parameter actually contains a save code (is not an empty variable),
    # then it goes into the options menu, goes into the import save menu, enters the save code into the input box,
    # exits the import save menu by pressing enter, and then continues onto the next step
        if save:
            time.sleep(2)
            # options menu
            options = bot.find_element_by_xpath('//*[@id="prefsButton"]')
            options.click()
            time.sleep(3)
            # import menu
            importsave = bot.find_element_by_xpath('//*[@id="menu"]/div[3]/div[3]/a[2]')
            importsave.click()
            # save code input box
            savefield = bot.find_element_by_xpath('//*[@id="textareaPrompt"]')
            savefield.send_keys(save)
            time.sleep(2)
            # enter button for input box
            enterSave = bot.find_element_by_xpath('//*[@id="promptOption0"]')
            enterSave.click()
            time.sleep(2)

        # finds the cookie
        cookie = bot.find_element_by_xpath('//*[@id="bigCookie"]')
        running = True

        # get the start time, then adds the amount of minutes (seconds muliplied by 60) to the start time 
        # and calls it the endtime
        starttime = time.time()
        stoptime = starttime + (float(run)*60)
        
        # while true, click on the cookie and then check if the current time is equal to the time it is supposed to stop
        # if it is, then break out of the loop.
        while running:
            cookie.click()
            if int(time.time()) == int(stoptime):
                break

   # GUI containing two input boxes
   # one for the save code (if wanted)
   # and one for the amount of time the user would like the auto clicker to run (required)         
root = Tk()

def start():
    clicker = AutoClicker()
    clicker.go(str(savecode.get()), timer.get())

savecodeLbl = Label(text="Enter your save code(optional): ")
savecodeLbl.pack()

savecode = Entry()
savecode.pack()

timerlbl = Label(text="Minutes to autoclick(required): ")
timerlbl.pack()

timer = Entry()
timer.pack()

gobtn = Button(text="Go", command=start)
gobtn.pack()

root.mainloop()
