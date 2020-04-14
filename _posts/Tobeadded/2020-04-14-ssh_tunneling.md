---
title:  "SHH tunneling"
excerpt: "GPU 서버의 resource를 로컬에서 사용하기"
toc: true
toc_sticky: true
toc_label: "목차"
use_math: true

categories: 
  - Environment
tags: 
  - Slurm
  - ssh tunneling
last_modified_at: 2020-04-14
---

***

현재 사용중인 데스크탑에는 오래된 GPU가 한 장 달려있는데, 
최근 [OpenPose]({{ site.url }}/deep%20learning/OpenPose_on_windows/)를 설치하다 GPU 메모리 부족으로 실패 한 적이 있다.
그래서 오늘은 GPU 서버에 있는 resource를 로컬에서 사용할 수 있도록 `ssh tunneling`을 시도해보려고 한다.

현재 사용중인 서버에는 총 8개의 GPU가 있고, [slurm]을 통하여 resource 관리가 되고 있다. 
기존에는 `docker`만 사용하다가 처음으로 `slurm`을 써보니 약간 불편하다는 생각이 든다. 
*slurm과 docker가 동일한 용도로 사용되는 프로그램인지는 잘 모르겠다.*
그래도 내가 관리하는 서버가 아니라 학교에서 관리하는 서버이고, 
거기다가 나는 무료로 사용하고 있으니 내가 맞출 수 밖에 없어서 최근에는 `slurm`을 공부하면서 서버를 사용하고 있다.
오늘은 이러한 과정 중 하나로 `ssh tunneling`과 `jupyter notebook`을 이용하여 로컬에서 서버의 resource를 사용하는 방법에 대해 정리해본다.  

***

# 1. slurm 명령어

지금까지 `slurm`을 쓰면서 가장 많이 쓴 명령어들을 정리해본다. 
명령어에 대한 정확한 설명이라기보다는 내가 느낀대로 해당 명령어를 설명해본다.

    srun: resource를 할당받아 job을 생성한다. (docker의 run)
    sattach: 현재 실행중인 job에 attach한다. (docker의 attach)
    sbatch: script를 backgroun로 실행시킨다. 
    squeue: 현재 실행중인 job을 보여준다. (docker의 ps)
    scancel: 실행중인 job을 중지한다. (docker의 stop)

# 2. SSH tunneling

기본적인 tunneling의 개념은 [포트 포워딩(SSH 터널링)의 개념 및 사용 방법]을 참고하였고,
slurm을 이용하여 jupyter notebook을 실행시키는 방법은 [SSH Port Forwarding and Jupyter Notebook]을 참고하였다.

# 2.1. Sever side

우선, resource를 할당받아 job을 생성하자.

```bash
[userid@master ~]$ srun -p gpu --gres=gpu:4 -J test --pty bash
[userid@node2 ~]$ 
```

그리고 할당받은 job내에서 anaconda environment를 실행시키자.

```bash
[userid@node2 ~]$ conda activate test
```

이제 `jupyter notebook`을 실행시키자.
`jupyter notebook`의 configuration setting은 [2.3. jupyter notebook setting](#23-jupyter-notebook-setting)을 참고하자.

```bash
[userid@node2 ~]$ jupyter notebook --config=~/.jupyter/jupyter_notebook_config.py
```

여기까지 하면 서버에서 할 일은 끝이 났다.
서버에서 한 일을 정리하면, 
resource를 할당받고 virtual environment를 이용하여 `jupyter notebook`을 실행시켜준 게 끝이다.

# 2.2. Client side

이제 로컬 컴퓨터를 이용하여 서버에서 실행시켜둔 `jupyter notebook`으로 접속하면 된다.
web browser에서 `jupyter notebook`에 접속하기 전에 ssh를 이용하여 서버와 로컬 컴퓨터 사이의 tunnel을 만들어주자.

```bash
ssh -N -f -L [로컬에서 사용할 포트]:[서버 내부 주소]:[서버의 포트(현재의 경우 8888)] [userid]@[서버주소] -p [포트번호]
```

ssh의 옵션으로 N, f, L을 사용하는데, 각각을 간단히 살펴보면[출처](http://linuxcommand.org/lc3_man_pages/ssh1.html),
* -N: remote command를 실행하지 않도록 하여 port forwarding할 때 사용하면 좋다
* -f: background에서 실행하도록 한다

예를 들면, 다음과 같이 접속하게 되면 데스크탑과 서버 사이의 tunnel이 생성된다.

```bash
ssh -N -f -L 8888:node2:8888 [userid]@[서버주소] -p [포트번호]
```

이제 web browser에서 jupyter notebok에 접속하자.
주소창에 `localhost:[ssh 연결시 설정한 로컬에서 사용할 포트]`을 입력하면 `jupyter notebok` 화면이 뜨는 것을 볼 수 있다.

# 2.3. jupyter notebook setting

`jupyter notebook`의 설정을 위해 `config` 파일부터 생성하자.

```bash
jupyter notebook --generate-config
```

위의 명령어를 실행하면 ~/.jupyter 경로에 `jupyter_notebook_config.py` 파일이 생성된 것을 볼 수 있다.
이제 이 파일을 수정하여 원하는 설정을 하도록 한다.
나는 다음의 설정들을 주석 해제와 함께 수정하였다.


```bash 
#Notebook에 모든 ip가 접속할 수 있도록 수정
#c.NotebookApp.ip = 'localhost' ==> c.NotebookApp.ip = '*' 

#jupyter notebook을 실행시켰을 때, web browser를 열지 않도록 수정
#c.NotebookApp.open_browser = True ==> c.NotebookApp.open_browser = False 

#jupyter notebook을 실행시킬 port를 8888 포트로 고정
#c.NotebookApp.port = 8888 ==> c.NotebookApp.port = 8888 

#jupyter notebook을 실행시켰을 때 보여지는 최상위 directory 설정 
#c.NotebookApp.notebook_dir = '' ==> c.NotebookApp.notebook_dir = '/home' 

#jupyter notebook 접속 비밀번호 설정
#c.NotebookApp.password = '' ==> c.NotebookApp.password = 'sha1:~' 
```

비밀번호 설정 방법은 bash shell에서 python을 실행하여 다음과 같이 진행하면 `sha1:~`의 암호화된 코드를 얻을 수 있고 이를 복사하여 `config` 파일의 password 부분에 넣어준다

```python
>>> from notebook.auth import passwd
>>> passwd()
Enter password:
Verify password:
'sha1:~'
```

***

# 참고자료
* [SSH Port Forwarding and Jupyter Notebook]
* [포트 포워딩(SSH 터널링)의 개념 및 사용 방법]
* [slurm]

[SSH Port Forwarding and Jupyter Notebook]: https://evcu.github.io/notes/port-forwarding/
[포트 포워딩(SSH 터널링)의 개념 및 사용 방법]: https://blog.naver.com/PostView.nhn?blogId=alice_k106&logNo=221364560794&parentCategoryNo=&categoryNo=22&viewDate=&isShowPopularPosts=false&from=postView
[slurm]: https://slurm.schedmd.com/

<!-- 
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.allow_root = True
-->
