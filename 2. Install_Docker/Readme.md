# Docker 설치 방법

<hr/>
- https://www.docker.com/ 에 접속하여 우측 상단의 GetStarted 버튼을 클릭후 다운로드 시작

<center><img src="1_get Strarted.PNG" width="1000" height="200"></center>

- 다운로드한 Docker를 설치하면서 회원가입 진행하며 설치가 완료되면 컴퓨터 재시작 진행
- 재시작후 재대로 설치되어있는지 확인 -> Terminal에서 Docker version 확인

# 만약 안될경우?

<hr/>

- 일반적으로 Windows에서 Docker를 진행할 경우 발생하는 2가지 문제.
1. **가상화 기능 활성화 유무**
2. **Hyper-V 옵션 활성화 유무**

- 제가 진행하면서 발생한 일반적이지 않은 문제
1. **WSL kernel 문제**
<center><img src="초기 WSL Kernel 문제.PNG" width="630" height="350"></center>

# 1. 가상화 기능 켜기

<hr/>

- 자신의 PC의 기상화 기능이 켜져있는지 확인 하기위해서는 작업관리자를 켜고 아래를 확인하면됩니다.
<center><img src="2_가상화 확인.PNG" width="400" height="400"></center>

- 만약 이러한 **가상화가 꺼져**있다면 컴퓨터 시작시  F12 or Del or F1등으로 접속할수있는 **BIOS화면**에서 수정이 가능합니다.
- 또한 사용하고있는 CPU에 따라 BIOS 화면이 다르기 때문에 사전에 확인해야한다.
- ASUS는 Intel Virtualization Technology로 표기하며 AMD는 SVM MODE로 표기하는 것처럼 다르니 조심하자!


<left><img src="AMD BIOS SVM.PNG" width="400" height="400"></left>        <rignt><img src="ASUS BIOS SVM.PNG" width="400" height="400"></right>


# Hyper-V 기능 켜기

<hr/>

- Hyper-V의 경우, [해당 사이트](https://windowsreport.com/hyper-v-and-containers-not-enabled/)를 참조하는 것이 좋을듯하다.
- 위 사이트의 내용을 요약하면 시도할 것은 총 2가지 입니다.
1. **Windows 기능에서 Hyper-V가 켜져있는지 확인하기**
2. **Windows PowerShell로 Hyper-V삭제 후 재설치**

<hr/>

# WSL kernel 문제
- 해당 문제는 Docker를 공부하기 위하여 기존 PC를 포맷하여 Windows 용 Linux가 부재
  - 리눅스가 설치되어있는지 확인하려면 터미널에서 WSL 명령어 입력
  <left><img src="WSL 명령어.PNG" width="500" height="200"></left>
- [필요한 Linux를 설치하고 설정](https://learn.microsoft.com/ko-kr/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package)해봅시다.
- 저는 Ubuntu 22.04.2 LTS를 설치하였습니다.
  
    <left><img src="우분투설치.PNG" width="450" height="150"></left>