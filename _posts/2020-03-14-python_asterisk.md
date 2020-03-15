---
title:  "Python - asterisk"
excerpt: "Python 코딩하면서 공부하고 이해한 내용을 정리, asterisk(*)"
toc: false
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Python
tags: 
  - asterisk
  - function
  - argument
last_modified_at: 2020-03-14
---

***

대학원 석사과정에서 처음 머신러닝을 시작할 때만 해도 Matlab으로 코딩을 진행했었다. 하지만 TensorFlow가 처음으로 release된 `2015-11-09` 이후부터는 Python과 Matlab을 혼용하여 사용하다가 이제는 Python으로 모든 코딩을 진행하고 있다. 이전 포스팅에서도 말했듯이 나는 컴퓨터 공학을 전공한 학생이 아니라 제대로 Python을 공부해본 적은 없다. 컴퓨터 언어를 제대로 공부해봤다고 그나마 얘기할 수 있는 건 `C` 정도인데, 포인터까지만 공부하고 그 뒤에 `malloc` 등의 메모리 관련된 부분은 시험 범위가 아니어서 공부를 제대로 하지 않았었다. 그리고 `Python`도 제대로 공부했다기보다는 그때그때 필요한 내용을 찾아가면서 이해를 하고 사용하고 있다. 그러한 과정에서 알게 된 내용을 정리해보고자 `Python` 포스팅을 시작하게 되었다.
> Python 포스팅은 `3.7 버전`을 기준으로 작성한다.

***

`Python` 첫 포스팅으로 다룰 내용은 `asterisk` 즉, `*`이다.  
```c
int num = 1;
int *var = &num; 
```
`C`에서는 위와 같이 주소 값을 저장하는 포인터 변수를 정의하는데 사용된다. 하지만 `Python`에서는 이와는 전혀 다른 의미로 사용된다. `Python` 코드를 보다보면 종종 함수에서 `*args`, `**kwargs`로 인자를 받는 경우를 볼 수 있을 것이다. `*`는 전달인자(argument)의 개수를 미리 정해놓지 않고 여러 개를 받을 수 있는 것을 의미한다. 그리고 여기서 `*`를 하나만 사용하면 사용하면 매개변수(parameter)에 전달되는 데이터의 형태가 <span style="color:purple">tuple</span> 로 전달 되는 것을 의미하고 `**`를 사용하면 <span style="color:purple">dictionary</span> 형태로 전달 되는 것을 의미한다. `*`와 `**` 뒤의 args, kwargs는 단순히 매개변수명이므로 원하는 이름으로 바꿔서 사용이 가능하다. 즉, `*_tuple`, `**_dict` 형태로도 사용이 가능하다.

> 보통 `*`와 `**` 뒤에 등장하는 args와 kwargs는 각각 arguments, keyword arguments를 의미한다. 

```python
def asterisk_test(*_tuple, **_dict):
  print(_tuple, _dict)
  
asterisk_test(1,2,3, p1='2', p2='3')
```

결과:

```python
(1, 2, 3) {'p1': '2', 'p2': '3'}
```



***
