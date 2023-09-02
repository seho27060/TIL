[TOC]

# Linux

## Service

- `Service`는 간단하게 머신 부팅시 자동으로 실행되는 프로그램이다.
  
  - 머신에서 `DB` 서버가 작동중일때, 머신을 부팅할때마다 `DB` 서버를 재실행해야한다. 만약 머신이 모종의 이유로 shutdown됐다면 재부팅이 될 수는 있으나, `DB`서버는 수동으로 재실행해줘야 할 것이다.

- `Service`에 필요한 작업을 할당하여 부팅시에 자동으로 시작할 수 있도록 한다.

- `Window`에서는 GUI로 간단하게 설정할 수 있고, `Linux`에서는 `service`, `systemd`, `systemctl`로 서비스를 등록할 수 있다.

- 머신에서 1개의 메인 어플리케이션이 동작중일때, 부하 관리와 같은 이유로 다른 프로세스에분리된 다른 서브 어플리케이션을 실행하고 싶을때 `service`에 서브 어플리케이션을 등록하여 1개 머신에서 2개의 어플리케이션을 동작할 수 있다.

#### Service 실행하기

- `service` 명령어로 새로운 서비스를 시작할 수 도 있지만,, `systemd`를 사용하는 OS버전에서는 `deprecated`되었다.

- `Linux`를 예시로 서비스 등록을 위해서는 서비스 설정을 위한 `.service` 파일에 형식에 맞게 설정을 할당한다.
  
  - 실행파일의 디렉토리, 재시도 등등 여러 옵션이 다양하다.
  
  - `systemd`로 `.service`파일로 원하는 serivce를 등록할 수 있으며, 해당 서비스들은 `/etc/systemd/system`에서 확인 할 수 있따.

- `systemctl`로 아래와 같이 수행할 수 있다.
  
  - ```bash
    systemctl 명령어 serviceName
    ```
    
    명령어로는 `start`, `restart`, `stop`, `status` 등등이 있다.

- `docker`나 여러 `CD` 툴로 `shell script`와 같이 사전에 정의한 명령어 묶음을 수행함으로 자동 배포, 실행이 가능하지만.. 그 이전에는 위와 같은 service 등록으로 수행했을지 모르겠다.

---

- 레퍼런스

> [[Linux] systemd란? (service 명령어, systemctl 명령어, init)](https://etloveguitar.tistory.com/57)
> 
> [service, systemctl 란?](https://junb51.tistory.com/9)
