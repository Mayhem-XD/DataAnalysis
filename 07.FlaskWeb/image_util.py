import numpy as np
from PIL import Image

# Pillow Format의 img를 읽어서 중심부의 이미지를 Pillow format으로 반환
def center_image(img):
    h,w,_ = np.array(img).shape
    diff = abs(h - w) // 2
    if w > h:
        final_img = np.array(img)[:,diff:diff+h,:]
    # portrait
    else:
        final_img = np.array(img)[diff:diff+w:]
    new_img = Image.fromarray(final_img)
    return ''

