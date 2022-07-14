# Docker 명령어

<hr/>
- 도커를 성공적으로 설치한 후 CMD 창을 켜서 각종 커맨드를 입력해보자
- 가장 기본적인 커맨드인 docker를 입력하면 다음과 같은 각종 커맨드와 옵션들이 나옵니다.
<left><img src="Basic_Docker_1.png" width="500" height="500"></left><right><img src="Basic_Docker_2.png" width="500" height="500"></right>

- 이중 오른쪽에 있는 Command에 대하여 주로 알아 보겠습니다.

1. Pull (image 다운로드) 
- docker hub에 존재하는 image를 다운받는 명령어입니다.
~~~terminal
docker pull alpine (alpine이라는 image를 docker hub에서 다운로드)
~~~

2. images  (현재 가지고 있는 image들의 목록 확인) 
- 1번 명령어를 사용하여 alpine이라는 image를 다운로드 받았으니 제대로 받았는지 확인해봅시다.
- 현재 유저가 가지고 있는 image들의 목록을 확인하는 명령어 입니다.  
~~~terminal
docker images 
~~~

3. run  (이미지를 사용하여 컨테이너를 생성하고 컨테이너에 접속) 
- run의 명령어는 기본적으로  docker run 옵션 이미지 명령어 ... 진행이 됩니다.

- 예를들어 **docker run alpine** 이라고 터미널에 작성하면  alpine 이미지로 컨테이너를 생성후 바로 끝날 겁니다.

- 이러한 run을 구동하기 위하여 필요한 옵션들을 먼저 알아봅시다.

  -  -i (--interactive) : 사용자가 컨테이너에서 입출력이 가능한 상태로 만들어줍니다. 
  - -t (--tty) : 컨테이너를 가상환경에서 에뮬레이션 하겠다는 의미입니다.
  - 위의 명령어는 동시에 사용하는 경우가 많아 2개를 합친것이 -it 입니다. 
  -  -d (--detach) : 컨테이너를 백그라운드에서 실행하겠다는 의미로 프로세스가 종료되도 컨테어너가 종료되지않고 살아있습니다
  - -p (--publish list) : 컨테이너의 포트를 호스트에 퍼블리쉬하겠다는 의미입니다. (ex -p 80:80 포트포워딩을 생각하시면됩니다.)
  - 더 많은 옵션들이 있지만 추후에 더 알아보도록 하겠습니다. 궁금하면 **docker run --help**를 입력하시면 나옵니다.



~~~terminal
docker run -p 3000:3000 -it alpine (localhost 3000포트에 퍼블리쉬하며 입출력형태로 컨테이너를 실행시키겠다)
docker run -p 4000:4000 -d alpine (localhost 4000포트에 퍼블리쉬하며 백그라운드에 출력시키겠다.)
~~~

