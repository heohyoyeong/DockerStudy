# Docker 설치 방법

<hr/>
- https://www.docker.com/ 에 접속하여 우측 상단의 GetStarted 버튼을 클릭후 다운로드 시작

<center><img src="1_get Strarted.png" width="1000" height="200"></center>
- 다운로드한 Docker를 설치하면서 회원가입 진행하며 설치가 완료되면 컴퓨터 재시작 진행
- 재시작후 재대로 설치되어있는지 확인 -> Terminal에서 Docker version 확인

# 만약 안될경우?

<hr/>

- 일반적으로 Windows에서 Docker를 진행할 경우 2가지 문제일 가능성이 있습니다.
1. **가상화 기능 활성화 유무**
2. **Hyper-V 옵션 활성화 유무**


# 가상화 기능 켜기

<hr/>

- 자신의 PC의 기상화 기능이 켜져있는지 확인 하기위해서는 작업관리자를 켜고 아래를 확인하면됩니다.
<center><img src="2_가상화 확인.png" width="400" height="400"></center>

- 만약 이러한 **가상화가 꺼져**있다면 컴퓨터 시작시  F12 or Del or F1등으로 접속할수있는 **BIOS화면**에서 수정이 가능합니다.
- 또한 사용하고있는 CPU에 따라 BIOS 화면이 다르기 때문에 사전에 확인해야한다.
- ASUS는 Intel Virtualization Technology로 표기하며 AMD는 SVM MODE로 표기하는 것처럼 다르니 조심하자!
<left><img src="AMD BIOS SVM.png" width="400" height="400"></left>        <rignt><img src="ASUS BIOS SVM.png" width="400" height="400"></right>



# Hyper-V 기능 켜기

<hr/>

- Hyper-V의 경우, 해당 사이트를 참조하는 것이 좋을듯하다. https://windowsreport.com/hyper-v-and-containers-not-enabled/
- 위 사이트의 내용을 요약하면 시도할 것은 총 2가지 입니다.
1. **Windows 기능에서 Hyper-V가 켜져있는지 확인하기**
2. **Windows PowerShell로 Hyper-V삭제 후 재설치**


