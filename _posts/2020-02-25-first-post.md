---
title:  "Github 블로그를 만들기"
excerpt: "Github 블로그 만들었던 과정을 정리"
toc: true

categories:
  - Blog
tags:
  - Blog
last_modified_at: 2020-02-26
---

***
대학원 석사과정을 졸업하고 회사에 취직을 했다가 다시 박사과정을 시작하면서 그동안 배웠던 것들을 정리하는 것이 필요하다고 느꼈다.  
기존에는 XMind나 Word 파일로 만들어뒀었는데 나만 본다고 생각하니 정리를 제대로 안 하게 되어 나중에 다시 보면 중간에 비어 있는 과정들이 너무 많은 것 같다.
그래서 그 과정을 정리..라기 보다는 그냥 과정을 기록하는 용도로 블로그를 사용하려고 한다.
이러한 이유로 첫 포스트는 이 블로그를 처음 만들었을 때의 과정을 기록하려 한다.

***

# 1. Jekyll 설치
Github 블로그를 만들려고 구글링을 해보니 Jekyll이란 이야기가 많이 나왔다. 제목은 다들 "Github 블로그 쉽게 만들기"인데 생각보다 과정이 너무 복잡한 것 같다. 난 단순한 자료를 찾고 싶은데 다들 제목은 쉽게 따라 하고 쉽게 만든다는데 설치하고 세팅하는 과정들이 많다고 느꼈다.   
*~~블로그를 만들고 보니 Jekyll을 설치하지 않아도 되는 것 같은데 일단 진행을 했던 부분이라 과정을 기록해본다. Jekyll로 서버를 실행해서 블로그를 띄우고 기타 등등을 하는 것 같은데 Gihub으로 블로그를 만드는 과정에는 필요가 없는 부분인 것 같다. Github 블로그를 쉽게 만드시려는 분들은 바로 다음 단계로 넘어가시면 됩니다.~~ 뒤에서 테마를 다운 받은 후 bundle 명령어를 해주지 않으면 404 error가 뜬다.* 

## 1.1. 윈도우에 Jekyll 설치하기
맥북과 윈도우 데스크탑을 같이 사용하고 있지만 듀얼 모니터로 연결된 윈도우 데스크탑이 편하다보니 윈도우 환경에서 블로그 만들기를 시작했다. 윈도우 환경에서 Jekyll을 설치하기 위해선 Ruby를 설치해야하는 것 같다. <https://rubyinstaller.org/downloads/> 에서 설치 파일을 다운로드 하자. 나는 해당 사이트에서 추천({{ page.last_modified_at }} 기준)하는 **Ruby+Devkit 2.6.X (x64)** 를 다운받았다.    

![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll1.png){: .align-center}*Ruby 설치파일 다운로드 사이트*

설치 중에 특별한 변경 사항 없이 기본 체크 사항으로 Next를 계속 눌러주었다.

![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll2.png){: .align-center}

설치가 완료되면 다음과 같은 창이 뜨는데 이때 그냥 Enter만 눌러주면 된다.
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll3.JPG){: .align-center}
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/1_1_install_jekyll4.JPG){: .align-center}

일단 여기까지 하면 Jekyll은 설치가 끝난듯 하다. ~~그런데 Jekyll을 설치했는데 이걸로 뭘 하는건지 잘 모르겠다.~~ 나중에 repository와 연결하기 전에 다운 받은 테마 폴더에서 bundle 명령어를 실행해줘야 블로그 화면을 띄울 수 있다.

## 1.2 Mac에 Jekyll 설치하기
Mac에서는 brew를 사용하여 설치할 수 있다. [참고](https://jekyllrb.com/docs/installation/macos/)
> \$ /usr/bin/ruby -e "\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
> $ brew install ruby

ruby path를 잡아주면 윈도우와 마찬가지로 ruby를 사용할 수 있다.
> export PATH=/usr/local/opt/ruby/bin:$PATH

ruby가 설치 되었는지 체크하자.
> $ ruby -v
ruby 2.6.3p62 (2019-04-16 revision 67580)

jekyll과 bundler를 설치하자.
> $ gem install --user-install bundler jekyll

***
# 2. Github 블로그 만들기
[Github](https://github.com)에 가입이 되어 있는 상태로 다음의 과정을 진행하고 혹시라도 Github에 가입이 안 되어 있으면 누구나 쉽게 가입할 수 있다. 

## 2.1. 내 Github에 repository 만들기
Github을 이용한 블로그들을 보면 대부분 "http://username.github.io"의 주소를 가지고 있으며, 이를 위해 나도 새로운 repository를 만들고 새로운 repository 이름을 "username.github.io"으로 만들었다.
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/2_1_make_repository.png){: .align-center}*{username}.github.io repository를 만들자*

## 2.2. 블로그 테마 선택하기
Github의 repository를 만들었으면 이제 http://jekyllthemes.org/ 에서 원하는 테마를 찾는다.
> 테마를 찾을 때 License를 조심하자. 확인을 해보지는 않았지만, 무료 License가 아닌 것이 있을수도 있다. License의 종류가 많이 있는것 같은데 다음에 기회가 되면 간단히 정리해봐야겠다.  

본 블로그는 무료 테마 중 사람들이 많이 사용 한다는 [minimal-mistakes](https://github.com/mmistakes/minimal-mistakes)를 사용하였다. 하지만 본 블로그는 이미 만들어졌기 때문에 새로운 블로그 테마 [Minimal Resume](http://jekyllthemes.org/themes/Minimal-Resume/)를 이용해서 다음의 과정들을 진행한다.
해당 테마를 선택한 후 Homepage 버튼을 눌러서 해당 테마의 Github 사이트로 이동하자.
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/2_2_select_theme.png){: .align-center}

## 2.3. 테마 다운
테마의 github으로 이동했으면 다음과 같은 화면이 보일 것이다.
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/2_3_theme_clone_download.png)
여기서 오른쪽에 보이는 녹색 버튼(Clone or download)을 클릭하여 해당 테마를 다운로드하거나 clone하자.
> [참고](https://devinlife.com/howto%20github%20pages/new-blog-from-template/): clone과 download의 차이는 clone은 기존의 git 히스토리를 모두 가져오지만 download는 그렇지 않다고 한다. 

해당 테마의 Github 사이트에서 바로 clone하거나 Terminal에서 command를 이용하여 clone을 하자. 나는 command를 이용해서 clone 하였다.
> $ git clone https://github.com/murraco/jekyll-theme-minimal-resume.git

## 2.5. 테마 폴더에서 bundle 명령어 실행
clone한 테마의 폴더로 이동하자.
> $ cd jekyll-theme-minimal-resume

테마 폴더에서 bundle 명령어를 실행하자.
> $ bundle

> [참고](https://devinlife.com/howto%20github%20pages/new-blog-from-template/): bundle 명령어를 실행하면 Gemfile이란 것을 검사해서 필요한 목록을 설치한다고 한다.

*bundle을 실행하지 않고 repository에 연결하니 404 error가 발생한다.*

## 2.4. 테마와 Github의 repository 연결하기
이제 테마를 내 repository에 연결할 차례이다.
테마를 clone하여 가져온 것이므로 기존의 remote origin을 제거한다.
> $ git remote remove origin

[2.1.](#2.1. 내 Github에 repository 만들기)에서 만든 repository를 등록하자.
> $ git remote add origin https://github.com/username/username.github.io.git

내 git repo에 소스가 업로드 되도록 push하자.
> $ git push -u origin master

여기까지 했으면 이제 나만의 블로그가 생성되었을 것이다. {username}.github.io을 통해 내 블로그에 접속하자.
![]({{ site.url }}{{ site.baseurl }}/assets/images/1.make_blog/2_4_blog.png)*내 블로그가 만들어졌다.*
***
# 참고자료
* Jekyll 설치 <https://soojae.tistory.com/16>
* Github 블로그 만들기 <https://devinlife.com/howto/>