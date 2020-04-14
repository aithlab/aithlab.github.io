---
title:  "OpenPose - Pose Estimation"
excerpt: "CMU의 OpenPose를 windows 10 환경에서 실행하기"
toc: true
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Deep Learning
tags: 
  - OpenPose
  - Key point detection
  - Pose estimation
  - Multi-person
  - Real time
last_modified_at: 2020-03-17
---

***

**진행해본 결과, windows10 에서 openpose를 설치하고 실행하기 위해선 Visual Studio 2017 Enterpreise 버전 설치가 필요했고, 4GB 이상의 GPU가 필요했다. 현재 가지고 있는 GPU가 2GB짜리여서 해당 포스팅에서는 OpenPose를 실행하는 결과까지는 확인하지 못했다. 대신 Windows portable version을 이용하여 간단히 Demo 정도만 돌려보았다.**

최근 진행 중인 연구에서 Key point detection을 사용할 일이 있어서 관련 open source를 찾아보았다. 여러 open source들이 있었지만 본 포스팅에서는 CMU에서 공개한 [OpenPose]를 사용해 보려한다. 그리고 해당 과정에서 발생하는 문제들을 해결하며 최종적으로 webcam에서 real-time으로 key point detction을 하는 것을 목표로 한다. 

> 해당 포스팅은 Windows 10 환경에서 진행하였고, 기회가 된다면 Mac OSX에서도 진행하여 관련 내용을 정리해보도록 하겠다.

***

# 1. OpenPose란?

[OpenPose]는 CMU에서 공개한 pose estimation(detection) 방법론이다. 
기술적인 자세한 내용은 아래의 논문을 참고하도록 하고, [OpenPose]에 대한 간단한 정보들을 [Github][OpenPose]에서 제공하는 내용을 바탕으로 살펴보자. 
[OpenPose]는 실시간으로 여러 사람의 pose estimation이 가능하고(물론 한 사람만도 가능하다), 사람의 몸, 손, 얼굴, 발의 총 135개 key point를 제공한다고 한다. 
*한 사람당 135개를 제공하는 듯 하다*. OpenPose에서는 크게 3가지의 detection block을 제공하고 있다. 

1. Body + Foot: 15/18/25개의 key point를 제공, Foot의 경우 6개 key point를 제공
2. Hand: 손 하나당 21개의 key point를 제공
3. Face: 총 70개의 key point를 제공

*25+21\*2+70=137인데, 앞서 총 135개의 key point를 제공한다고 했으니 아마 Hand와 Body에서 겹치는 부분이 있는 것이 아닌가 생각된다.*

각 block의 running time의 경우 감지된 사람에 따라 다르다고 한다. 
2D 영상의 경우 여러 사람에 대한 detection이 가능하지만 3D의 경우는 한 사람에 대한 detection만 가능하다고 한다.

<figure>
<img align='center' src="{{ site.url }}{{ site.baseurl }}/assets/images/8.openpose_on_windows/1_1_openpose_example.gif" >
<figcaption>OpenPose 예시(출처:OpenPose github)</figcaption>
</figure>

> Cao, Z., Hidalgo, G., Simon, T., Wei, S. E., & Sheikh, Y. (2018). OpenPose: realtime multi-person 2D pose estimation using Part Affinity Fields. arXiv preprint arXiv:1812.08008.

# 2. OpenPose 설치하기

[OpenPose]의 doc.를 확인해보면 Windows 10뿐만 아니라 Ubuntu, Mac OSX, Nvidia Jetson 등에서 OpenPose의 실행이 가능한 것으로 보인다. 해당 doc에서 제공하는 Windows 10 환경에서의 OpenPose 설치 과정을 따라가보자.

## 2.1. Windows에서 CMake GUI 설치하기

**본 포스팅에서는 GPU 메모리 용량의 부족으로 인해 OpenPose를 Windows 10에 설치하는 것을 실패하였다. 여기서 설치를 한다는 것은 향후 OpenPose 코드를 수정하거나 새로운 데이터 등으로 학습 시키기위한 용도로 사용함을 의미하며, 만약 단순히 Pre-trained 모델을 이용하여 webcam, video 또는 images에서 key-point detection 결과만을 확인하고 싶다면 [2.3. Windows portable version 실행하기](#23-windows-portable-version-실행하기)를 따라가자.**

우선, 설치 과정 중 제일 첫 번째로 `OpenPose`를 Build해야한다. 보통 Linux에서는 cmake로 build가 가능하지만, Windows 10에서는 한 번도 해본 적이 없어 다른 open source를 찾아볼지 잠시 고민을 했지만 Windows 환경에서도 CMake가 가능하다고 한다. 그리고 GUI 형식으로 지원하기 때문에 어렵지 않게 느껴졌다.  
<https://cmake.org/download/>로 접속하여 `Platform`에 있는 파일 중 자신의 환경에 맞는 설치 파일을 다운로드 하자. 나는 {{ page.last_modified_at }}을 기준 제일 위에 있는 `Windows win64-x64 Installer`를 받아서 설치를 진행하였다. 설치 과정 중에 option들은 default로 설치하였다. **나의 경우, 기존에 Visual Studio 2019가 설치되어 있어 따로 설치를 진행하지는 않았지만 cmake를 실행하기 위해 Visual Studio가 필요하다. OpenPose 공식 doc에서는 Visual Studio 2017 Enterprise 또는 VS 2015 Enterprise Update 3 버전 사용을 권장하는 듯 하다.** ~~나는 2019 버전이 이미 설치되어 있으므로 이를 이용하여 다음의 설치 과정들을 따라가보자.~~ 2019 버전을 사용하면 Build 과정에서 `build/OpenPose.sln` 파일 실행이 되지 않는다. `Visual Studio 2017 Enterprise`를 다운받아 설치하자!

> `Visual Studio 2019` 버전을 사용하여 진행하면 openpose 폴더 안에 있는 몇 개의 파일들이 지원되지 않는 형식이라고 오류가 뜬다.

## 2.2. CMake GUI 이용해서 Build하기

> CMake란([참고](https://eunmink.tistory.com/6))? 오픈 소스들을 다루다 보면 CMake가 자주 등장한다. 그럴때마다 별 생각없이 README에서 시키는 대로 진행하였는데, 포스팅을 하는 김에 간단히 CMake가 무엇인지 찾아보았다. 우선 CMake는 Cross platform Make의 약자라고 한다. 단어를 풀어놓으니 어느정도 와닿는 것 같다. 말 그대로 platform간에 이동을 쉽게 해주는 빌드 시스템 제너레이터라고 한다.

설치 과정은 [OpenPose]에서 제공하는 [설치 doc](https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/master/doc/installation.md#Installation)을 따라간다.  

설치된 CMake GUI를 실행하여 다음의 그림과 같이 source code를 openpose 폴더로 설정해주고 build할 위치를 openpose 폴더 내에 build라는 폴더를 새로 만들어 해당 경로로 잡아주자.

<img align="center" src="{{ site.url }}{{ site.baseurl }}/assets/images/8.openpose_on_windows/2_2_cmake_build1.JPG">

그리고 아래의 `Configure` 버튼을 눌러 다음의 그림과 같이 설치된 Visual Studio 버전과 optional platform for generator를 `x64`로 꼭 세팅해주고 Finish를 눌러주자.  
(`Visual Studio 2017 Enterprise`를 다운받아 `Visual Studio 15 2017`로 세팅하자!)

<p align="center">
<img src="{{ site.url }}{{ site.baseurl }}/assets/images/8.openpose_on_windows/2_2_cmake_build2.JPG">
</p>

그러면 build에 필요한 파일이나 complier 등을 체크할 것이다. `Configure`를 실행하면 windows 환경의 dependencies 중 파일들을 다운로드 하는 장면이 등장하는데 여기서 시간이 오래걸렸다. CMake GUI에서는 다운로드 받는다고만 하고 얼마나 남았는지 등의 정보가 보이지 않아 해당 사이트에 직접 접속하여 다운 받아보니 130MB 파일을 다운받는데 예상 시간이 대략 30~40분이다.. 일단 기다려 보았다. 그런데 하나가 아니라 여러 개를 받아야한다.. 기다렸다..  근데 기다려도 다운이 안 된다.. 결국 다운 받아야하는 파일들을 각각 사이트로 직접 들어가서 다운 받아 openpose 폴더 안에 다음과 같이 넣어주었다.

    - <http://posefs1.perception.cs.cmu.edu/OpenPose/3rdparty/windows/opencv_411_v14_15_2019_09_24.zip>: download & unzip in `openpose-master\3rdparty\windows` 
    - <http://posefs1.perception.cs.cmu.edu/OpenPose/3rdparty/windows/caffe3rdparty_15_2019_03_14.zip>: download & unzip in `openpose-master\3rdparty\windows` 
    - <http://posefs1.perception.cs.cmu.edu/OpenPose/3rdparty/windows/caffe_15_2019_05_16.zip>: download & unzip in `openpose-master\3rdparty\windows` 

    - [BODY_25 model](http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/body_25/pose_iter_584000.caffemodel): download in `models/pose/body_25/`.
    - [COCO model](http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/coco/pose_iter_440000.caffemodel): download in `models/pose/coco/`.
    - [MPI model](http://posefs1.perception.cs.cmu.edu/OpenPose/models/pose/mpi/pose_iter_160000.caffemodel): download in `models/pose/mpi/`.
    - [Face model](http://posefs1.perception.cs.cmu.edu/OpenPose/models/face/pose_iter_116000.caffemodel): download in `models/face/`.
    - [Hands model](http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel): download in `models/hand/`.

`Configure`가 완료 되면 다음의 그림과 같이 "Configuring done"이 보일 것이다. 그러면 `Generate` 버튼을 눌러주자. 마찬가지로 "Generating done"이 보일 것이다.
<img align="center" src="{{ site.url }}{{ site.baseurl }}/assets/images/8.openpose_on_windows/2_2_cmake_build3.JPG">

`build/OpenPose.sln`을 **Visual Studio 2017 enterprise 버전**으로 실행하고, configuration을 Debug에서 `Release`로 변경하여 Run하자.

여기서 나는 cuda의 out of memory가 발생하였다. 4GB이상의 GPU가 필요하다.

## 2.3. Windows portable version 실행하기

[OpenPose]에서 [portalble version](https://github.com/CMU-Perceptual-Computing-Lab/openpose/releases)을 다운받자. {{ page.last_modified_at }}를 기준으로 총 4개의 파일이 존재한다. 

    openpose-1.5.1-binaries-win64-gpu-python-flir-3d_recommended.zip
    openpose-1.5.1-binaries-win64-gpu-python-flir-3d_unity.zip
    openpose-1.5.1-binaries-win64-only_cpu-python-flir-3d.zip
    openpose-1.5.1-binaries-win64-only_cpu-unity.zip

파일 이름 중간에 `gpu`가 포함되어 있는 파일의 경우 `gpu`를 사용하도록 되어 있어 앞선 상황과 동일하게 `out of memory`가 발생한다. 
portable version이지만 마찬가지로 4GB 이상의 GPU가 필요한 듯 하다.
그래서 나는 `cpu` 버전으로 다운을 받았다. `cpu` 버전도 두 가지가 있는데, 뒤에 `unity`가 붙은 파일의 경우 파일이 없다고 오류가 발생한다. 
파일의 이름으로 생각해봤을 때, `unity`를 사용하게끔 만들어진 파일이 아닐까 싶다. 
따라서, 나는 `openpose-1.5.1-binaries-win64-only_cpu-python-flir-3d.zip`를 이용하여 실행하였다.
[portable version 실행 doc][Running on Webcam]를 살펴보면 Portable Demo의 경우 다음과 같이 실행할 수 있다.

    :: Windows - Portable Demo
    bin\OpenPoseDemo.exe
    :: With face and hands
    bin\OpenPoseDemo.exe --face --hand

하지만 다운받은 그대로 실행을 해보면 model이 없다고 오류가 뜰 것이다. 
앞서 [CMake GUI 이용해서 Build하기](#22-cmake-gui-이용해서-build하기)에서 받은 모델이 필요하다. 
나의 경우 앞선 과정에서 다운을 받아둔 상태라 해당 폴더(openpose/models)를 그대로 복사해왔다.
만약 다운받지 못하였으면, `openpose/models` 안에 있는 `getModels.bat` 파일을 실행하면 자동으로 다운받을 수 있다.

다운을 받았다면, openpose 폴더에서 `bin\OpenPoseDemo.exe`를 실행하면 webcam을 통해 [OpenPose]가 실행되는 것을 볼 수 있다.
하지만 GPU를 사용하지 않는 버전이라 그런지 FPS가 0으로 표시된다.(0으로 표시되지만 실제는 0보다 더 낮은 듯 하다.)

***

# 참고자료
* OpenPose: <https://github.com/CMU-Perceptual-Computing-Lab/openpose>
* CMake: <https://eunmink.tistory.com/6>

[OpenPose]: https://github.com/CMU-Perceptual-Computing-Lab/openpose
[Running on Webcam]: https://github.com/CMU-Perceptual-Computing-Lab/openpose/blob/v1.5.1/doc/quick_start.md#running-on-webcam