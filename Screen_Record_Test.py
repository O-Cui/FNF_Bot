import numpy as np
import cv2
from mss import mss
from PIL import Image
import time

bounding_box = {'top': 100, 'left': 0, 'width': 400, 'height': 300}

sct = mss()

while True:
    t0 = time.time()
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))
    print("fps: {}".format(1 / (time.time() - t0)))
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break