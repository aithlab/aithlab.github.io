---
title:  "PyCharm 사용하기"
excerpt: "Python 코딩을 위해 PyCharm IDE 사용해보기"
toc: true
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Python
tags: 
  - IDE
  - pycharm
last_modified_at: 2020-03-16
---

***

새로운 언어를 시작하게 되면 제일 먼저 접하게 되는 것이 어디에 코딩을 할 것인가이다. 가장 기초적인 방법으로는 그냥 text파일 하나 열어서 코딩을 하면 될 것이다. 하지만 시중에는 이미 좋은 Editor들과 IDE(Integrated Development Environment)가 많이 존재하기 때문에 사람들이 많이 쓰고 내가 쓰기 편한 것을 골라 코딩을 시작하게 된다. 나는 Python을 제일 처음 접했을때 아무것도 모르는 상태로 Python을 설치했더니 `IDLE`가 함께 설치되어 `IDLE`를 이용하여 코딩을 했었는데, `Matlab`을 사용하다가 `IDLE`로 Python 코딩을 하다보니 다시 `C`로 돌아간 기분이 들었었다. `Matlab`을 사용하면서 가장 좋았고 편했던게 variable explorer가 있다는 것이었다. variable explorer를 통해 그때 그때 바로 값을 확인할 수 있어서 디버깅하기 쉬웠는데 `IDLE`는 그런 variable explorer가 없어서 많이 답답했었다. 그러다가 우연히 `Spyder`를 알게 되고 variable explorer를 지원하는 것을 알게되어 그 이후로는 쭉 `Spyder`를 사용해왔다. 그리고 최근에는 `Jupyter Notebook`도 자주 사용하는데 `Jupyter Notebook`은 뭔가 실제 코딩 보다는 수업에서 step-by-step으로 실행할 때나 세미나때 사용하기 좋은 것 같다. 그리고 본 포스팅에서는 `PyCharm` 사용법에 대해 다뤄보려고 한다. 뜬금없이 `PyCharm`을 사용해보려는 이유는 우선 많은 사람들이 `PyCharm`을 사용하기도 하고 얼마 전부터 Google에서 시험을 통해 [TensorFlow certificate](https://www.tensorflow.org/certificate)을 발급한다고 하는데 이 시험을 위해서는 `PyCharm`을 사용해야한다는 조건이 있기 때문이다. 박사과정을 시작하면서부터 기존 `TensorFlow`에서 `PyTorch`로 넘어와서 TensorFlow certificate 시험을 볼지는 모르겠지만, 아무래도 Google에서 발급하는 것이다보니 기회가 되면 테스트를 보는 것도 좋을 것 같아 `PyCharm`에 익숙해져보려고 한다.

> IDE와 Editor 차이: IDE는 Integrated Development Environment의 약자로써 

***

# 1. Editor/IDE 종류

`PyCharm`을 시작하기 전에 Pyhon 코딩을 위해 어떤 Editor/IDE들이 있는지 간단히 찾아보았다. 

* Sublime Text
* Visual Studio Code (VS code)
* VI / VIM
* PyCharm
* Jupyter Notebook
* Spyder

위의 항목들이 대충 사람들이 많이 사용하는 Editor/IDE인것 같다. 가장 많이 사용하는 Editor/IDE는 조사하는 사람마다 다를 것 같아 위의 순서는 신경쓰지 않았다. 위의 리스트를 보니 사람들이 많이 사용하는 Editor/IDE들을 사용해본 것 같다. `Sublime Text`는 예전에 `java script`할 때 많이 써봤고, `VS code`는 지금도 `Markdown`이나 가끔 코드 확인용으로 사용하고 있고 `Jupyter Notebook`, `Spyder`는 많이 사용해오고 있다. `VI`는 `Linux` 환경에서는 많이 사용해봤지만 python 코딩을 `VI`로 해본 것은 예전에 회사에 있을 때 어떤 강의를 갔다가 강사님이 `VI`로 python 코딩을 하셔서 그때 사용해본 적이 있다. `VI`도 세팅을 잘 하면 다른 Editor/IDE 처럼 변수나 함수를 색깔로 표시하는 것도 가능하고 나름 편하게 사용할 수 있었던 기억이 있다. 각 Editor/IDE마다 나름의 장점도 있을 것이고 각자 편한 환경이 다를 것이므로 사용해보고 각자 취향에 따라 선택하면 될 것 같다. 나는 Variable explorer가 있는게 편해서 `Spyder`를 주로 사용했지만 `Jupyter Notebook`에서도 약간의 Variable explorer를 제공하고 `PyCharm`에서도 제공하는 것 같아 `PyCharm`을 사용해보고자 한다.

# 2. PyCharm 설치하기

`PyCharm` 설치는 간단하다. <https://www.jetbrains.com/pycharm/>에서 `Community` 버전으로 다운 받으면 된다. `Professional` 버전의 경우, 유료이고 설명상으로는 `Community` 버전 보다 더 많은 것들(Scientific, Web Python)을 지원하는 것 같다. 하지만 `PyCharm`을 처음 접해보는 입장에서는 그냥 `Community` 버전을 다운 받아 사용해보자. 학교 계정을 이용하면 `Professional` 버전도 무료로 사용이 가능한 듯 하나, 일단 `Community` 버전을 설치하자.

설치 시에 나오는 옵션들은 모두 default로 설치하였다. 그리고 `PyCharm`을 실행하면 다음의 화면이 보인다.

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/9.use_pycharm/2_pycharm1.JPG">

사실 여기서 조금 해맸다. 주로 쓰는 `Spyder`의 경우 Project의 개념이 없어서 그냥 실행 파일만 열면 되는데 `PyCharm`에서는 project를 열라고 하는데 난 파일만 열고 싶고.. 일단 `PyCharm`에서 원하는대로 project를 하나 만들어 보았다. python 파일을 하나 만들어서 `Hello World`를 print 해봤는데 오류가 났다. Interpreter를 설정해주자!

# 3. Python Interpreter 설정하기

`File > Settings > Prject: username > Project interpreter`으로 이동하면 다음의 화면을 볼 수 있다. 현재는 interpreter 설정이 되어있지 않아 설치된 Package들이 보이지 않는다. 옆에 있는 톱니바퀴를 눌러 `Show All...`을 선택하자.  

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/9.use_pycharm/3_interpreter1.png">

마찬가지로 Interpreter에 아무것도 보이지 않는다. 옆에 있는 `+` 버튼을 눌러 interpreter를 추가해주자.

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/9.use_pycharm/3_interpreter2.png">

나는 기존에 `Anaconda`를 설치하여 Python을 이용하고 있었으므로 `Anaconda`에 설치된 Python 경로를 잡아주었다.

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/9.use_pycharm/3_interpreter3.JPG">

Interpreter를 잡아주고 이전 화면으로 나와보니 아까는 아무것도 보이지 않던 package들이 보이기 시작했다.

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/9.use_pycharm/3_interpreter4.JPG">

python 파일을 하나 만들어서 Hello world를 출력해보자.

<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/9.use_pycharm/3_interpreter5.JPG">

제대로 프린트가 되는 것을 확인하였다. 이로써 `PyCharm` 설치 및 세팅은 완료된 듯 하다. 

***

# 참고자료
* Editor/IDE 종류: <https://www.programiz.com/python-programming/ide>
* Editor/IDE 종류: <https://realpython.com/python-ides-code-editors-guide/>