# TEXT TO SPEECH

# import gtts
# from playsound import playsound
#
# tts = gtts.gTTS("Hello world")
# tts.save("hello.mp3")
# playsound("hello.mp3")
#
# # SCREEN SHARING
#
import pyautogui
# im2 = pyautogui.screenshot('my_screenshot2.png', region=(0,0,1920,1080))

# DETECTING MOUSE CLICKS

from pynput.mouse import Button, Controller
#
# mouse = Controller()

# Read pointer position
# print('The current pointer position is {0}'.format(
#     mouse.position))

# Set pointer position
# mouse.position = (10, 20)
# print('Now we have moved it to {0}'.format(
#     mouse.position))

# mouse.click(Button.left, 2)

from pynput.mouse import Listener

# def on_move(x, y):
#     print('Pointer moved to {0}'.format(
#         (x, y)))
#
#
# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#     # if not pressed:
#     #     # Stop listener
#     #     return False
#
#
# def on_scroll(x, y, dx, dy):
#     print('Scrolled {0}'.format(
#         (x, y)))


# Collect events until released
# with Listener(
#         # on_move=on_move,
#         on_click=on_click) as listener:
#     # on_scroll=on_scroll)
#     listener.join()

# OPTICAL CHARACTER RECOGNITION
# import cv2
# import pytesseract
#
# img = cv2.imread('image.jpg')
#
# # Adding custom options
# custom_config = r'--oem 3 --psm 6'
# print(pytesseract.image_to_string(img, config=custom_config))

# from pynput.mouse import Listener
#
# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#         'Pressed' if pressed else 'Released',
#         (x, y)))
#
#
# with Listener(on_click=on_click) as listener:
#     listener.join()

import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('fullPage1.jpg')
custom_config = r'--oem 3 --psm 1'
string = pytesseract.image_to_string(img, config=custom_config)
dict = pytesseract.image_to_data(img, output_type=Output.DICT,
                                 config=custom_config)

yCoord = 0
xCoord = 0
counter = 0
xLis = []
yLis = []
maxX = 0
for text, top, left, width, height in zip(dict["text"], dict["top"],
                                          dict["left"], dict["width"],
                                          dict["height"]):
    if text in ["The", "cat", "(Felis", "catus)"]:
        if counter == 1:
            yCoord = top
            xCoord = left
        counter += 1

    if counter >= 1 and yCoord - 10 < top < yCoord + 10:
        # img = cv2.rectangle(img, (left, top), (left + width, top + height),
        #                     (0, 255, 0), 2)
        xLis.append(left)
        yLis.append(top)
        if left == max(xLis):
            maxX = left + width
    elif counter >= 1 and xCoord - 10 < left < maxX:
        # img = cv2.rectangle(img, (left, top), (left + width, top + height),
        #                     (0, 255, 0), 2)
        xLis.append(left)
        yLis.append(top)
img = cv2.rectangle(img, (min(xLis), min(yLis)), (max(xLis), max(yLis)),
                    (255, 0, 0), 2)
print(pytesseract.image_to_string(img, config=custom_config))
cv2.imshow('img', img)
cv2.waitKey(0)