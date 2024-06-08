import streamlit as st
import numpy as np
import cv2
from PIL import Image

cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

image_file = st.sidebar.file_uploader('画像アップロード, (jpg, jpeg, png)',type=['jpg', 'png','jpeg'])

print(type(image_file))
if image_file:
    if st.sidebar.button('プレビュー'):
        image = Image.open(image_file)
        st.sidebar.image(image)
    if st.sidebar.button('検出'):
        image_bytes = image_file.getvalue()
        np_array = np.frombuffer(image_bytes, dtype= np.uint8)
        img = cv2.imdecode(np_array, flags = cv2.IMREAD_COLOR)
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        facerect = cascade.detectMultiScale(rgb_image)
        for i, rect in enumerate(facerect):
            cv2.rectangle(rgb_image,
                          tuple(rect[0:2]),
                          tuple(rect[0:2] + rect[2:4]),
                          (255,0,0),thickness=2)
            x, y, w, h = rect
            cropped_image = img[y:y+h, x:x+w]
            cv2.imwrite(f'test{i}.jpg', cropped_image)
            print(x, y, w, h)
        st.image(rgb_image, use_column_width=True)
    