---
title:  "Github 블로그를 만들기"
excerpt: "Github 블로그 만들었던 과정을 정리"

categories:
  - Blog
tags:
  - Blog
last_modified_at: 2020-02-26
---

대학원 석사과정을 졸업하고 회사에 취직을 했다가 다시 박사과정을 시작하면서 그동안 배웠던 것들을 정리하는게 필요하다고 느꼈다.  
기존에는 XMind나 Word 파일로 만들어뒀었는데 나만 본다고 생각하니 정리를 제대로 안 하게 되어 나중에 다시 보면 중간에 비어 있는 과정들이 너무 많은 것 같다.
그래서 그 과정을 정리..라기 보다는 그냥 과정을 기록하는 용도로 블로그를 사용하려고 한다.
이러한 이유로 첫 포스트는 이 블로그를 처음 만들었을때의 과정을 기록하려 한다.

# 1. Jekyll 설치
Github 블로그를 만들려고 구글링을 해보니 Jekyll이란 이야기가 많이 나왔다. 제목은 다들 "Github 블로그 쉽게 만들기"인데 생각보다 과정이 너무 복잡한거 같다.  
*블로그를 만들고 보니 Jekyll을 설치하지 않아도 되는거 같은데 일단 진행을 했던 부분이라 과정을 기록해본다. Jekyll로 서버를 실행해서 블로그를 띄우고 하는거 같은데 Gihub으로 블로그를 만드는 과정에는 필요가 없는 부분인것 같다. Github 블로그를 쉽게 만드시려는 분들은 바로 다음 단계로 넘어가시면 됩니다.* 

## 1.1. 윈도우에 Jekyll 설치하기
맥북과 윈도우 데스크탑을 같이 사용하고 있지만 듀얼 모니터로 연결된 윈도우 데스크탑이 편하다보니 윈도우 환경에서 블로그 만들기를 시작했다. 윈도우 환경에서 Jekyll을 설치하기 위해선 Ruby를 설치해야하는 것 같다. rubyinstaller.org/downloads 에서 설치 파일을 다운로드 하자. 나는 해당 사이트에서 추천({{ page.last_modified_at }} 기준)하는 **Ruby+Devkit 2.6.X (x64)** 를 다운받았다.    

![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll1.png)*Ruby 설치파일 다운로드 사이트*

설치 중에 별 다른 변경 사항 없이 기본 체크 사항으로 Next를 계속 눌러주었다.

![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll2.png)
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll3.png)
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll4.png)
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll5.png)



# 참고자료


블로그를 처음 시작하면서 블로그에 어떤 내용을 담아야할지 고민을 해보았다.  
우선 블로그를 시작하게된 이유는 
"{{ page.title }}"의 명령어를 쓰면 제목이 보인다: {{ page.title }}  
"{{ page.last_modified_at }}"의 명령어를 쓰면 수정된 시간이 보인다: {{ page.last_modified_at }}
