import numpy as np
import cv2
from mss import mss
from PIL import Image
import time
import pyautogui
import pydirectinput
import keyboard

bounding_box = {'top': 50, 'left': 1020, 'width': 680, 'height': 230}

def canny_blur(base_temp):
    
    gblur  = cv2.GaussianBlur(base_temp,(5, 5),cv2.BORDER_DEFAULT)
    final = cv2.Canny(gblur, 75, 255)
    return final
t_last = time.time()

la_pressed = True
ra_pressed = True
da_pressed = True
ua_pressed = True


def key_input(y_loc):
    global t_last, la_pressed, da_pressed, ua_pressed, ra_pressed
    if y_loc < 170:
        if la_pressed == False:
            pydirectinput.press('left')
            la_pressed = True
            print('left')
        else:
            la_pressed = False
    elif y_loc < 340:
        if da_pressed == False:
            pydirectinput.press('down')
            da_pressed = True
            print('down')
        else:
            da_pressed = False
        
    elif y_loc < 510:
        if ua_pressed == False:
            pydirectinput.press('up')
            ua_pressed = True
            print('up')
        else:
            ua_pressed = False
    elif y_loc < 680:
        if ra_pressed == False:
            pydirectinput.press('right')
            ra_pressed = True
            print('right')
        else:
            ra_pressed = False
    t_last = time.time()


la = cv2.imread("C:\\Users\\User\\3D Objects\\Downloads\\la.PNG", 0)
ra = cv2.imread("C:\\Users\\User\\3D Objects\\Downloads\\ra.PNG", 0)
ua = cv2.imread("C:\\Users\\User\\3D Objects\\Downloads\\ua.PNG", 0)
da = cv2.imread("C:\\Users\\User\\3D Objects\\Downloads\\da.PNG", 0)

temp_list = []
temp_load = [la, ra, ua, da]

for temp in temp_load:
    temp_list.append((temp))
sct = mss()
paused = True
while True:
    if keyboard.is_pressed('q'):
        paused = False
    
    while not paused:
        t0 = time.time()

        
        scr_img = cv2.cvtColor(np.array(sct.grab(bounding_box)), cv2.COLOR_BGR2GRAY)
        #scr_img = canny_blur(scr_img_gr)

       
        img2 =  scr_img.copy()
        for template in temp_list:
            
            h, w = template.shape

            result = cv2.matchTemplate(img2, template, cv2.TM_SQDIFF_NORMED)
            
            
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
            location = min_loc
            bottom_right = (location[0]+w, location[1]+h)
            
            if location[1] > 20 and location[1] < 100:
                key_input(location[0])

                
            cv2.rectangle(img2, location, bottom_right, 255, 1)
            cv2.imshow("Match", img2)

        print("fps: {}".format(1 / (time.time() - t0)))
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
        if keyboard.is_pressed('e'):
            paused = True





