import matplotlib.pyplot as plt
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image

img_path = './Lenna.png'
img_cv2 = cv2.imread(img_path) # BGR
img_pil = Image.open(img_path) # RGB
img_matplotlib = plt.imread(img_path) # RGB, float32
img_tf = tf.io.decode_png(tf.io.read_file(img_path))

print((np.array(img_pil) == img_cv2).all(0).all(0))
> [False  True False]

print((np.array(img_pil)  == cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)).all(0).all(0))
> [ True  True  True]

print((np.array(img_pil)  == np.array(img_matplotlib*255, np.uint8)).all(0).all(0))
> [ True  True  True]

print((np.array(img_pil)  == np.array(img_tf)).all(0).all(0))
> [ True  True  True]


img_rgb = np.array(cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB))

plt.figure()
plt.title('Original image')
plt.imshow(img_rgb)
plt.axis('off')

plt.figure()
plt.title('Reversed image (y-axis)')
plt.imshow(img_rgb)
plt.axis('off')
plt.gca().invert_yaxis()

plt.figure()
plt.title('Reversed image (x-axis)')
plt.imshow(img_rgb)
plt.axis('off')
plt.gca().invert_xaxis()

plt.figure()
plt.title('Reversed image (x and y axis)')
plt.imshow(img_rgb)
plt.axis('off')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

