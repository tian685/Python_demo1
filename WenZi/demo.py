#   ---*- coding: utf-8 -*-
#  ￥- *--- author---祥彪--￥
import cv2
from WenZi import img_str
if __name__=='__main__':
    #创建窗口，固定的
    cv2.namedWindow("camera",1)
    capture = cv2.VideoCapture(0)
    while True:
        success,img = capture.read()
        cv2.imshow("camera",img)
        key = cv2.waitKey(100)
        if key == 27:
            print('esc break')
            break
        if key == 32:

            filename = 'frames.jpg'
            cv2.imwrite(filename,img)
            s = img_str.img_to_str(filename)
            print(s)

    capture.release()
    cv2.destroyWindow("camera")
