import pyautogui
from time import sleep
import random
from PIL import Image, ImageGrab
#pyautogui.displayMousePosition()

# identify if there is an open building slot - done
# if there is an open slot open the building menu - done
# if there is an optional build - build it 
# check if if there is still place in the building column
# if there there is look for the next possilbe build
# if there is no build in the first line scroll down until you see an optional build or you reach the end
# if there is a possiblr build - build it if not - close the build window
# keep running this process in a loop that will wait for a build slot to open.

openBuildSlotImage = r"C:\Users\Michael\Documents\Python\web-projects\game_automation\tw\build_slot_open_on_map.png"
upgradeToImage = r"C:\Users\Michael\Documents\Python\web-projects\game_automation\tw\upgrade_to.png"
scrollBarImage =  r"C:\Users\Michael\Documents\Python\web-projects\game_automation\tw\scroll_bar.png"
scrollEndImage = r"C:\Users\Michael\Documents\Python\web-projects\game_automation\tw\scroll_end.png"

def seek_and_build_coutinously():
    # wait until building slot opens
    while pyautogui.locateOnScreen(openBuildSlotImage, grayscale = True, confidence = 0.9) is None:
        pass
    # when this loop ends the build slot is visible
    print("I see build slot")
    print("sleeping")
    sleep(random.random()*3)
    print("finished sleeping")
    # locate the build slot location and open it
    location =  pyautogui.locateOnScreen(openBuildSlotImage, grayscale = True, confidence = 0.9)
    if location is None:
        seek_and_build_coutinously()
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x, y, random.random(), pyautogui.easeOutQuad)
    pyautogui.click(x, y)
    print("sleeping")
    sleep(random.random()*3)
    print("finished sleeping")
    # look for build option
    if pyautogui.locateOnScreen(upgradeToImage, grayscale = False, confidence = 0.95) is None:
        scroll_end_found = pyautogui.locateOnScreen(scrollEndImage, grayscale = True, confidence = 0.9)
        # if the scroll ended close the window
        if scroll_end_found is not None:
                print("I see scroll end")
                pyautogui.press('esc')
                print("sleeping")
                sleep(random.random()*60*5)
                print("finished sleeping")
        scroll_location = pyautogui.locateOnScreen(scrollBarImage, grayscale = True, confidence = 0.8)
        if scroll_location is None:
            print("cant see scroll bar")
            seek_and_build_coutinously()
        print("cab't see build options, sleeping")
        sleep(random.random()*3)
        print("finished sleeping, scrolling down")
        scroll_location = pyautogui.center(scroll_location)
        x, y = scroll_location[0], scroll_location[1]
        sleep(random.random()*3)
        pyautogui.moveTo(x, y, random.random(), pyautogui.easeOutQuad)
        print("sleeping")
        sleep(random.random()*3)
        print("finished sleeping")
        pyautogui.drag(0, 100, random.random(), pyautogui.easeOutQuad, button='left')
        pyautogui.mouseUp()
        #pyautogui.scroll(-50000) 
        print("sleeping")
        sleep(random.random()*3)
        print("finished sleeping")
        seek_and_build_coutinously()
    else:
        location =  pyautogui.locateOnScreen(upgradeToImage, grayscale = False, confidence = 0.95)
        if location is None:
            seek_and_build_coutinously()
        #for location in locations:
        #  x, y = pyautogui.center(location)
        x, y = location[0], location[1]
        pyautogui.moveTo(x, y, random.random(), pyautogui.easeOutQuad)
        print(f"x: {x}, y: {y}")
        #im = Image(pyautogui.screenshot())
        screen_width, screen_height = pyautogui.size()
        bbox = (0, 0, screen_width, screen_height)
        im = ImageGrab.grab(bbox)
        coords = int(x), int(y)
        px = im.getpixel(coords)
        print(px)
        pyautogui.moveTo(x, y, random.random(), pyautogui.easeOutQuad)
        pyautogui.click(x, y)
        print("sleeping")
        sleep(random.random()*3)
        print("finished sleeping")
        pyautogui.press('esc')
        seek_and_build_coutinously()

seek_and_build_coutinously()

print("script finished")




