---
title:  "GitHub 블로그 - Liquid"
excerpt: "블로그에서 {%, %}, {{, }} 텍스트로 표시하기"
toc: true
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Blog
tags: 
  - Blog
  - Liquid
last_modified_at: 2020-02-29
---

***
{% raw %}
이전 포스팅에서 수식 입력을 위해 수정해야 하는 내용을 다뤘다. 이때 수정해야 하는 것들을 작성하면서 `{%, %}`를 포함하는 코드가 있었는데 해당 부분이 블로그에 표시되지 않는 문제가 발생하였다. 이러한 문제가 발생한 이유는 Jekyll은 템플릿 처리를 위해 [Liquid] 언어를 사용하는데 Liquid에서는 `{{ ~ }}` 형태를 통해 변수를 출력하고, `{% ~ %}` 형태를 통해 논리문(logic statements)을 수행하기 때문인 것 같다. 그래서 블로그에 `{{ ~ }}``{% ~ %}`를 작성하려고 하면 해당 내용을 텍스트로 받아들이는 게 아니라 명령어로 받아들여 논리문을 실행하고 변수를 출력하게 된다.
{% endraw %}

> GitHub pages는 Jekyll을 내부 엔진으로 사용해서 블로그를 GitHub에 호스팅할 수 있게 한다고 한다. [참고 자료][Jekyll 참고]

***

# 1. Liquid 문법 표시하기
{% raw %}
`{{ ~ }}`,`{% ~ %}`
{% endraw %}
형태를 텍스트로 표시하기 위해서는 <img src="{{ site.url }}{{ site.baseurl }}/assets/images/4.blog_liquid/1_sentence1.png">, <img src="{{ site.url }}{{ site.baseurl }}/assets/images/4.blog_liquid/1_sentence2.png">와 같이 앞과 뒤에 raw, endraw를 추가해주면 된다.
{% raw %}`{{ page.title }}`{% endraw %}에 대해서 raw와 endraw를 포함한 경우와 포함하지 않은 경우의 결과를 확인해보겠다.

raw와 endraw없이 했을 경우

```
{{ page.title }}
```

raw와 endraw를 추가했을 경우

{% raw %}
```
{{ page.title }}
```
{% endraw %}

***


[Liquid]: https://jekyllrb.com/docs/liquid/
[참고자료]: https://stackoverflow.com/questions/24102498/escaping-double-curly-braces-inside-a-markdown-code-block-in-jekyll

[Jekyll 참고]: https://github.com/gud2great/unistclub/wiki/%EC%A7%80%ED%82%AC(Jekyll)%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EA%B8%B0%EC%88%A0%EB%B8%94%EB%A1%9C%EA%B7%B8-%EB%A7%8C%EB%93%A4%EA%B8%B0