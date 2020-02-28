---
title:  "Github 블로그 수정하기"
excerpt: "Github 블로그를 운영하면서 필요한 것들을 정리 - 수식 입력"
toc: true
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Blog
tags: 
  - Blog
  - Markdown
last_modified_at: 2020-02-28
---

***

처음에 Github 블로그를 만들어야겠다고 생각했을 때는 많은 시간을 뺏기지 않을 정도의 내용들을 데코레이션없이 담자고 생각했었다.
하지만 포스팅을 하다보니 조금 더 이쁘게 하고 싶은 욕심도 생기고, 수식이나 내용의 배열들을 작성함에 있어서 Jupyter Notebook에서 간단히 다뤘던 Markdown을 더 깊게 다루는 것 같다.
그래소 본 포스팅에서는 Github 블로그를 처음 만들고 몇 개의 포스팅을 하면서 필요했던 간단한 내용들을 참고 자료와 함께 작성해보려 한다.

***

# 1. 수식 입력하기

Jupyter Notebook에서는 단순히 `$ ~ $` 형태로 inline 수식을 입력하거나 `$$ ~ $$`로 수식을 입력했었다.
하지만 Jekyll 테마를 이용하여 Github 블로그를 만들고 당연히 수식이 입력될 줄 알고 Jupyter Notebook에서 사용하던대로 썼는데 수식입력이 되지 않았다. 
내가 받은 테마만 기본적으로 세팅이 되지 않은 건지 아니면 다른 Jekyll 테마들도 세팅이 되지 않은건지 정확히 알 수는 없지만 중요한 문제는 아니고 그냥 단순히 세팅을 추가해주면 되는 것이라 해당 자료를 찾아 수식 입력이 가능하도록 세팅을 하였다. 수식 입력하는 방법은 [[GitHub] Github 블로그 수식 추가 (kiko-now)][수식 입력하기]를 참고하였고, 아래의 내용도 해당 블로그에서 가져온 내용이다.

1\. _config.yml 수정하기
블로그 관련 자료들이 있는 제일 상위 폴더에 존재하는 `_config.yml` 파일을 수정해주어야 한다.

```md
# Conversion
markdown: kramdown
highlighter: rouge
lsi: false
excerpt_separator: "\n\n"
incremental: false
```

[내가 받은 테마](https://github.com/mmistakes/minimal-mistakes)의 경우 위의 세팅은 기본적으로 되어 있었다.

2\. mathjax_support.html 파일 만들기
`_includes` 폴더 안에 새로운 파일을 만들어주어야 한다. `mathjax_support.html`이란 파일을 새로 만들고 아래의 내용을 추가하자.

```html
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    TeX: {
      equationNumbers: {
        autoNumber: "AMS"
      }
    },
    tex2jax: {
    inlineMath: [ ['$', '$'] ],
    displayMath: [ ['$$', '$$'] ],
    processEscapes: true,
  }
});
MathJax.Hub.Register.MessageHook("Math Processing Error",function (message) {
	  alert("Math Processing Error: "+message[1]);
	});
MathJax.Hub.Register.MessageHook("TeX Jax - parse error",function (message) {
	  alert("Math Processing Error: "+message[1]);
	});
</script>
<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>
```

3\. head.html 수정하기
`_includes` 폴더 안에 이미 존재하는 `head.html` 파일에 다음의 내용을 추가해주자.

```html
{% if page.use_math %}
  {% include mathjax_support.html %}
{% endif %}
```

4\. 수식 입력이 가능하도록 포스트에 옵션 추가하기
포스트를 만들때 다양한 옵션들이 있겠지만 나는 처음 포스트를 만들때 참고했던 [사이트](https://devinlife.com/howto%20github%20pages/first-post/)에서 사용하는 옵션만을 사용하고 있었다. 여기에 `use_math: true` 항목만 추가적으로 입력해주면 수식을 사용할 수 있다.

```md
---
title: ~
excerpt: ~
use_math: true

categories:
  - ~
tags:
  - ~
last_modified_at: ~
---
```

위와 같은 세팅 과정을 거치면 Jupyter Notebook에서와 같이 `$ ~ $` 또는 `$$ ~ $$`로 수식 입력이 가능하다.  
예)  
`$ ~ $`:

$\times $, $\int$, $\sigma$, $alpha$  

`$$ ~ $$`:

$$ N(\mu, \sigma)={1 \over \sqrt{2\pi\sigma^2}}exp({-{1 \over 2\sigma^2}} (x-\mu)^2) $$  

***

# 참고자료
* [수식 입력하기][수식 입력하기]

[수식 입력하기]: https://blog.naver.com/PostView.nhn?blogId=prt1004dms&logNo=221525385428&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
