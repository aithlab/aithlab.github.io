---
title:  "Python - Data path"
excerpt:  "Python 코딩하면서 공부하고 이해한 내용을 정리, Data path "
toc: true
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Python
tags: 
  - path
last_modified_at: 2020-04-11
---

***

`Python`으로 코딩을 하다보면 Data를 불러오는 장면을 많이 만나게 된다. 본 포스팅에서 Data를 불러오기 위해 `Path`를 잡아줄 때 사용할 수 있는 방법을 적어본다.

> Python 포스팅은 `3.7 버전`을 기준으로 작성한다.

***

# 1. Data load

Data를 불러오는 라이브러리는 데이터의 형태에 따라 다양하게 있다.

* Image 파일 - opencv, pillow, matplotlib, TensorFlow, ... [Python - 이미지 처리 포스팅 참고]({{ site.url }}{{ site.baseurl }}/python/python_image_read_show/)
* Audio 파일 - wave, scipy, pydub, ..
* 엑셀 파일 - pandas, xlrd, ...

위의 데이터 형태는 지금 생각나는 가장 기본적인 형태들과 해당 형태의 데이터를 읽기 위해 필요한 라이브러리들을 나열해보았다. 
본 포스팅에서는 Data load와 관련해서는 직접적으로 다루지 않으려 한다. 
다만 모든 Data load 과정에서 필요한 데이터의 `Path`를 잡아줄 때 사용할 수 있는 `os` 모듈을 정리해보고자 한다.

> 모듈? 라이브러리? 차이: 포스팅을 쓰다보니 모듈(Module)과 라이브러리(Library)의 용어에 혼돈이 왔다. 지금까지는 '라이브러리'라는 단어만을 주로 사용해왔는데, python document를 보다보니 '모듈'이라는 단어도 등장하는 것을 보았다. 일단 결론적으로는 **모듈, 라이브러리는 거의 동일하게 사용**되는 듯 하다. 함수나 클래스들을 취합하여 재사용하기 편하게 만든 코드들의 집합을 모듈, 라이브러리라고 정의한다고 한다. 따라서, 향후의 포스팅에서는 모듈과 라이브러리라는 단어를 혼용하여 사용하도록 한다. 주로 '라이브러리'를 사용하겠다.

# 2. os 라이브러리로 데이터 path 잡아주기

나는 주로 데이터의 Path를 잡아줄 때 `os` 라이브러리를 사용한다. 구글링을 하다보면 종종 `glob`도 많이 사용되는 것을 볼 수 있지만, 우선적으로는 외우기 쉽게 하나의 라이브러리만 쭉 사용해보고 있다.  
os 라이브러리에서 많이 사용하는 함수들은 다음과 같다.

# 2.1. path 잡을 때 주로 사용하는 함수

* os.listdir(path): path에 속해있는 파일 및 폴더를 리스트 형태로 반환
* os.path.join(root_path, file_name): `os.listdir` 함수로 폴더 내의 파일 이름(file_name)을 가져와 폴더의 경로(root_path)와 연결하여 file의 전체 path를 잡아줄 때 사용
* os.path.splitext(path): path에서 확장자와 나머지를 분리하여 특정 확장자만 읽어올 때 사용
* os.path.isdir(path): path가 폴더인지 아닌지 반환하는 함수로 폴더 안에 있는 폴더로 접근 할 때 주로 사용
* os.path.exists(path): path가 존재하는지 확인하는 함수
* os.path.dirname(file_path): 파일이 위치하는 경로 반환
* os.path.abspath(file_path): 파일의 절대 경로 반환
* 파일의 시간을 체크하는 함수
  * os.path.getctime(file_path): 파일의 change 시간을 반환 (제일 최근 체크포인트를 가져올때 유용)
  * os.path.getatime(file_path): 파일의 access 시간을 반환 
  * os.path.getmtime(file_path): 파일의 modification 시간을 반환

> Access - the last time the file was read  
> Modify - the last time the file was modified (content has been modified)  
> Change - the last time meta data of the file was changed (e.g. permissions)  
> Modify Change 차이점: modify의 경우 file의 content가 변경되는 것을 의미하고, change의 경우 content 뿐만 아니라 권한 등의 변경 시간을 보여준다.  
> 출처: [getctime, getmtime, getatime 차이]  


# 2.2. 그 외 주로 사용되는 함수

* os.mkdir(path): 디렉토리 만들기
* os.makedirs(path, exist_ok=False(default)): `os.mkdir`과 동일하지만 하위 디렉토리도 함께 만들어 줄 수 있음 (exist_ok를 False로 할 경우, 이미 디렉토리 존재하면 OSError 발생, True로 할 경우, 존재해도 ok)
* os.path.basename(path): path에서 파일명(확장자 포함)만 추출하는 함수
* os.getcwd(): 현재 작업 디렉토리 출력

이 외에도 코딩을 하다가 자주 사용되는 함수가 있으면 계속 추가하여 작성하려 한다.

***

# 참고자료
* 모듈 vs. 라이브러리: <https://brownbears.tistory.com/437>
* <https://wikidocs.net/3717>
* [ctime, mtime, atime 차이](https://unix.stackexchange.com/questions/2802/what-is-the-difference-between-modify-and-change-in-stat-command-context)
