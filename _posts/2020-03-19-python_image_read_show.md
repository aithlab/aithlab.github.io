---
title:  "Python - 이미지 처리"
excerpt: "라이브러리별 image read 비교 및 matplotlib 축 반전시키기"
toc: true
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Python
tags: 
  - Image
  - matplotlib
  - Deep learning
last_modified_at: 2020-03-19
---

***

이미지, 영상 등은 딥러닝 분야에서 많은 부분을 차지하고 있다. 
그리고 딥러닝을 처음 배우는 사람들도 제일 먼저 접하는 분야가 이미지 분류 문제일 것이다.
이에 따라, `Python`에서도 이미지 파일을 다루기 위한 라이브러리가 다양하게 있다.  
대표적으로 많이 사용하는 라이브러리들은 `opencv`, `pillow`, `matplotlib` 등이 있을 것 같다. 
각자의 취향, 편의성 마다 주로 사용하는 라이브러리가 다르겠지만 본 포스팅에서는 딥러닝에서 이미지를 다룰 때 사용하는 라이브러리들을 간단히 비교하려 한다. 

***

# 1. 이미지 읽어오기

이미지 관련 딥러닝을 하기 위해서 제일 첫 번째로 해야하는 것은 바로 이미지 파일을 읽어오는 것이다. 
이때 이미지 파일을 읽기 위한 라이브러리들은 다양하게 있고 각자의 취향마다 주로 사용하는 라이브러리가 다르겠지만, 
본 포스팅에서는 다음 4개의 라이브러리를 이용하여 이미지 파일을 읽어왔을 때의 형식을 비교한다.

* opencv (version: 4.1.1.26)
* pillow (version: 7.0.0)
* matlpotlib (version: 3.1.1)
* TensorFlow (version: 2.1.0)

> 1. [참고](https://www.kaggle.com/vfdev5/pil-vs-opencv)에 따르면, 처리 속도에서 pillow 보다 opencv가 더 빠르다고 한다.
> 2. PyTorch(torchvision)에서는 내부적으로 pillow를 backend로 이용한다.[참고](https://github.com/pytorch/vision#image-backend)

각각의 라이브러리에는 이미지를 읽기 위한 함수가 존재한다.
`opencv`에서는 `cv2.read`, `pillow`에서는 `Image.open` 그리고 `matplotlib`에서는 `plt.imread`를 통해 이미지를 불러올 수 있다. 
또한, `TensorFlow2`에서는 `tf.io.read_file(img_path)`를 통해 이미지 파일을 읽어온 후  `tf.io.decode_png`, `tf.io.decode_jpeg` 등을 통해 이미지를 불러올 수 있다.
각 라이브러리들을 통해 이미지를 불러왔을 때의 `type`, `dtype`, `image order`는 다음과 같다.

    opencv
      - type: numpy.ndarray
      - dtype: uint8, [0, 255]
      - image order: BGR

    PIL
      - type: PIL.PngImagePlugin.PngImageFile
      - dtype: uint8, [0,255]
      - image order: RGB
      
    matplotlib
      - type: numpy.ndarray
      - dtype: float32, [0,1]
      - image order: RGB

    TensorFlow
      - type: tensorflow.python.framework.ops.EagerTensor
      - dtype: float32, [0,255]
      - image order: RGB

**opencv의 경우 BGR 순서인 것을 주의하자!**
> [참고](https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/)에 따르면 opencv가 만들어질 당시 회사에서 BGR 순서를 많이 사용했다고 한다.


# 2. Matplotlib에서 이미지 확인하기

마찬가지로 이미지를 `show`하기 위해선 각 라이브러리마다 지원하는 함수가 존재한다. 
`opencv`에서는 `cv2.imshow`, `pillow`에서는 `{image_file}.show()`, `matplotlib`에서는 `plt.imshow`를 통해 이미지를 `show`할 수 있다. 
**opencv에서는 cv2.read로 이미지를 읽어오면 BGR 순서로 읽어오기 때문에 cv2.imshow에 들어가는 이미지의 색상 순서도 BGR로 되어 있어야 한다.**  
각자 취향에 따라 이미지를 `show`하겠지만, 나같은 경우에는 `matplotlib`을 주로 사용한다. 
많이 사용해봐서 익숙한 것도 있지만 이미지 위에 `plot` 등을 함께 사용할 경우가 가끔 있기 때문이다.
`matplotlib`에서 `plot`을 이용할 경우, 일반적으로 y축의 아래 부분이 0 값으로 세팅이 된다. 
하지만 `imshow`를 이용할 경우, y축의 윗 부분이 0 값으로 세팅이 된다는 것을 주의하자.
이는 이미지의 경우 일반적으로 y축의 윗 부분이 0값을 가지기 때문이다.

간단한 예제로 영상 처리 등에서 많이 사용되는 [Lenna](https://en.wikipedia.org/wiki/Lenna) 이미지를 사용하여 테스트 해보자.

```python
img_path = './Lenna.png'
img = cv2.imread(img_path) # BGR
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```

`opencv`를 통해 이미지를 읽어왔으므로 `RGB 순서`로 변경해준다.

```python
plt.figure()
plt.title('Original image')
plt.imshow(img_rgb)
plt.axis('off')
```

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/10.python_image_read_show/original.png">

## 2.1. 이미지 반전 시키기

데이터 Augmentation을 위해서 가끔 반전 등을 사용할 때가 있다. 
보통 `PyTorch`나 `TensorFlow`등에서 augmentation을 위한 함수들이 함께 제공될테지만, 간단하게 `matplotlib`을 통해 확인할 수 있는 방법을 소개한다.
`plt.gca().invert_yaxis()`, `plt.gca().invert_xaxis()`를 사용하면 된다.

```python
plt.figure()
plt.title('Reversed image (y-axis)')
plt.imshow(img_rgb)
plt.axis('off')
plt.gca().invert_yaxis()
```

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/10.python_image_read_show/reverse_y.png">

```python
plt.figure()
plt.title('Reversed image (x-axis)')
plt.imshow(img_rgb)
plt.axis('off')
plt.gca().invert_xaxis()
```

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/10.python_image_read_show/reverse_x.png">

```python
plt.figure()
plt.title('Reversed image (x and y axis)')
plt.imshow(img_rgb)
plt.axis('off')
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
```

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/10.python_image_read_show/reverse_xy.png">


***


# 참고자료
* <https://www.it-swarm.dev/ko/python/pyplot%EC%9D%98-y-%EC%B6%95-%EC%97%AD%EB%B0%A9%ED%96%A5/968738380/>
* <https://note.nkmk.me/en/python-opencv-bgr-rgb-cvtcolor/>
* <https://www.learnopencv.com/why-does-opencv-use-bgr-color-format/>