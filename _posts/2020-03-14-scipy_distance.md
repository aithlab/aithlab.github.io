---
title:  "Python - SciPy(pdist, squareform)"
excerpt: "Scipy의 pdist, squareform을 이용하여 distance 쉽게 구하기"
toc: false
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Python
tags: 
  - SciPy
  - distance
last_modified_at: 2020-03-14
---

***

 `Python`에서 다수의 포인트들끼리의 거리를 구하기 위한 방법은 다양하게 있을 것이다. 본 포스팅에서는 다수의 포인트들끼리의 거리를 구하기 위한 방법 중 하나로 `scipy`를 이용하는 방법을 정리하고자 한다. 각자 본인의 코딩 스타일마다 알맞는 방법이 많을 것이므로 앞으로 소개하고자 하는 방법이 가장 best는 아니겠지만, 한 줄로 표현이 가능하고 나름 편한 방법이라 생각되어 정리해두려 한다.

***

앞으로의 예시를 위해 다음과 같이 2차원 공간의 point 50개가 있다고 가정하자.

```python
import numpy as np

pts = np.randm.random([50,2])
```

이러한 각 포인트들끼리의 거리(distance)를 따져야하는 상황이 발생했다고 하자. 그리고 각 포인트들끼리의 거리 계산 결과가 `50x50` 형태 즉, `포인트 개수(N) x 포인트 개수(N)`의 형태를 가지게 하여 직관적으로 각 포인트들끼리의 거리를 확인하고 싶다고 하자.  
이전의 나는 아마 `np.zeros`등으로 빈 행렬을 만든 후 `numpy.linalg.norm`를 이용하여 각 포인트들끼리의 거리를 계산하여 행렬에 넣어줬을 것이다. 하지만 scipy에서 제공하는 `pdist`와 `squareform`을 이용하니 비교적 쉽게 각 포인트들끼리의 계산이 가능한 것을 확인하였다. 

```python
from scipy.spatial.distance import pdist, squareform

pairwise_dists = pdist(pts, metric='euclidean')
pts_dists = squareform(pairwise_dists)
```

`pdist` 함수의 경우 각 포인트들끼리의 거리를 pair-wise로 계산해준다. 이때 거리를 계산하는 방법은 위의 코드에서 표시한 `euclidean`외에 `cosine`, `hamming` 등 다양한 방법이 존재한다. `pdist`를 이용하여 각 포인트끼리의 거리를 계산했으므로 이를 사용할 수도 있을 것이다. 하지만 `pdist`의 결과가 저장된 pairwise_dists 변수의 형태를 살펴보면 `(1225,)` 형태를 가지고 있을 것이다. 50개 포인트끼리의 거리를 계산했는데 직관적으로 생각했을때 50x50 또는 자기 자신과의 거리를 제외한 49x49 형태를 가져야할 것 같은데 `(1225,)` 형태를 가지고 있다. 1225란 숫자는 49+48+47+...+1에서부터 나온 결과이고, 이로부터 유추할 수 있는 `pdist`의 결과물은 첫 번째 포인트와 나머지 포인트들끼리의 거리를 계산 한 후, 두 번째 포인트와 나머지 포인트끼리의 거리를 계산할 때는 첫 번째 포인트를 제외하고 계산하고 나머지 계산들도 동일하게 진행되어 1225란 숫자가 나온 것이다. 이러한 pairwise_dists 변수를 `squareform` 함수에 넣어주면 기존에 원했던 `50x50` 형태로 만들 수 있다.  
한줄로 쉽게 사용하려면 다음과 같이 사용하면 된다.

```python
dists = squareform(pdist(pts, metric='euclidean'))
```

***

# 참고자료
* [scipy.spatial.distance.pdist](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.distance.pdist.html)
* [scipy.spatial.distance.squareform](https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.spatial.distance.squareform.html)
