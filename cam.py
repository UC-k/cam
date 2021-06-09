import streamlit as st
import cv2
import time
from PIL import Image

st.markdown('# カメラアプリ')

flg = 1

radio = st.radio(
    'text',
    ('run', 'stop')
)

if radio == 'run':
    flg = 0
elif radio == 'stop':
    flg = 1

device = user_input = st.text_input('input your video/camera device', '0')
if device.isnumeric():
    device = int(device)

cap = cv2.VideoCapture(device)
# cap = cv2.VideoCapture(0)

image_loc = st.empty()

while cap.isOpened:
    if flg == 0:
        ret, img = cap.read()
        time.sleep(0.01)
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        image_loc.image(img)

    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    if flg == 1:
        break

cap.release()