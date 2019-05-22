import cv2
import numpy as np
import pyautogui

from tkinter import *

start_flag = True


# Magic code. I don't know how it works
def nothing (x):
    pass
#Удаляет все открытые фреймы
def destroyWindows():
    video.release()
    cv2.destroyAllWindows()


video = cv2.VideoCapture(0)

pointX = 0
pointY = 0

img = np.zeros((300, 512, 3), np.uint8)



H = 0
S = 0
V = 0
H_shag = 20
S_shag = 80
V_shag = 60

H_min = 0
H_max = 0
S_min = 0
S_max = 0
V_min = 0
V_max = 0


def ActivateController (H_, S_, V_, H_flag, S_flag, V_flag, StartMouse, height_screen, width_screen):

    global H, S, V, H_min, H_max, S_min, S_max, V_min, V_max



    #Получение видео
    _, frame = video.read()

    width_video = video.get(3)
    height_video = video.get(4)

    #Удаление шумов
    blurred_frame = cv2.GaussianBlur(frame, (5, 5), 0)
    #преобразование в HSV
    hsv = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

    print(H_flag, S_flag, V_flag)
    if H_flag:
        H_min = H_
        H_max = H_min + H_shag
        if H_max > 255:
            H_max = 255
    else:
        H_min = 0
        H_max = 255

    if S_flag:
        S_min = S_
        S_max = S_min + S_shag
        if S_max > 255:
            S_max = 255
    else:
        S_min = 0
        S_max = 255

    if V_flag:
        V_min = V_
        V_max = V_min + V_shag
        if V_max > 255:
            V_max = 255
    else:
        V_min = 0
        V_max = 255



    lower_blue = np.array([H_min, S_min, V_min])
    upper_blue = np.array([H_max, S_max, V_max])


    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        area = cv2.cv2.contourArea(contour)
        if area > 400:
            img2 = cv2.drawContours(frame, contour, -1, (0, 255, 3))
            rect = cv2.boundingRect(contour)
            #рисуем прямоугольник
            cv2.rectangle(frame, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 0, 255), 2)
            if StartMouse:
                MouseMove(width_screen, width_video, height_screen, height_video, rect)
                cv2.circle(frame, (pointX, pointY), 5, (0, 255, 0))

    cv2.imshow("Frame", frame)

    cv2.imshow("mask", mask)

def MouseMove(width_screen, width_video, height_screen, height_video, rect):

    global pointX, pointY

    width_video = int(width_video * 0.7)
    height_video = int(height_video * 0.7)

    # Вычисляем коэфиценты для экрана и видео
    k_width = width_screen / width_video
    k_height = height_screen / height_video

    #1 точка прямоугольника
    x1 = int(rect[0])
    y1 = int(rect[1])
    #2 точка прямоугольника
    x2 = int((rect[0] + rect[2]))
    y2 = int((rect[1] + rect[3]))

    if pointX < x1:
        pointX = x1
        if pointX < 0: pointX = 0
    elif pointX > x2:
        pointX = x2
    if pointY < y1:
        pointY = y1
        if pointY < 0: pointY = 0
    elif pointY > y2:
        pointY = y2

    pointMouse = pyautogui.position()
    pointMouseX = int(pointMouse.x)
    pointMouseY = int(pointMouse.y)

    # двигаем мышь
    pyautogui.moveTo(width_screen - (pointX * k_width - width_screen * 0.2), pointY * k_height - height_screen * 0.2)




