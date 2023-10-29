- [PCB/ Context Switching](#pcb-context-switching)
  - [Process Control/Context Block](#process-controlcontext-block)
    - [Process Management](#process-management)
    - [PCB(Process Control/Context Block)](#pcbprocess-controlcontext-block)
  - [Context Switching](#context-switching)
    - [Context](#context)
    - [OverHead](#overhead)
    - [인터럽트(Interrupt)](#인터럽트interrupt)

# PCB/ Context Switching

## Process Control/Context Block

### Process Management

> CPU가 프로세스가 여러개일 때, CPU 스케줄링을 통해 관리하는 것

- 이때 CPU는 각 프로세스들이 어떤것인지 알아야 관리가 가능하다. 프로세스 정보를 갖는 데이터를 `Pocess Metadata`이다.

- `Process Metadata`
  
  - Process ID
  
  - Process State
  
  - Process Priority
  
  - CPU Registers
  
  - Owner
  
  - CPU Usage
  
  - Memory Usage
  
  메타데이터는 프로세스가 생성되면 `PCB`에 저장된다.

### PCB(Process Control/Context Block)

> 프로세스 메타데이터들을 저장해 놓은 곳, 하나의 PCB안에는 하나의 프로세스의 정보가 담긴다.

- CPU에서는 프로세스의 상태에 따라 교체 작업이 이뤄진다. 
  
  - ex) interrupt가 발생한 프로세스가 waiting 상태가 되고 다른 프로세스를 running으로 교체

- `Linked List`방식으로 관리되며, PCB List Head에 PCB들이 생성될 때마다 추가된다. 주소값으로 연결이 이뤄진 연결리스트이기 때문에 삽입 삭제가 용이하다.
  
  - 프로세스 생성시 해당 PCB가 생성되고, 프로세스 완료시 제거된다.
  
  - 프로그램 실행 - 프로세스 생성 - 프로세스 주소 공간에 메타데이터 생성 - 메타데이터를 PCB에 저장 과 같은 과정을 거친다.

- 위와 같이 수행중인 프로세스를 변경할 떄, CPU의 레지스터 정보가 변경되는 것을 `Context Switching`이라고 한다.

## Context Switching

> CPU가 이전의 프로세스 상태를 PCB에 보관, 또 다른 프로세스 정보를 PCB에 읽어 레지스터에 적재하는 과정
> 
> 여러개의 프로세스([멀티프로세스]([TIL/CS/Operating System/220915 프로그램, 프로세스, 스레드 at master · seho27060/TIL · GitHub](https://github.com/seho27060/TIL/tree/master/CS/Operating%20System/220915%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%A8%2C%20%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%2C%20%EC%8A%A4%EB%A0%88%EB%93%9C)))가 실행될 때, 기존에 실행중인 프로세스를 중단하고 다른 프로세스를 실행하는 것. CPU에 실행할 프로세스를 교체하는 기술

- 보통 진행중인 프로세스에 대해 인터럽트가 발생하거나, 실행 중인 CPU 사용 허가 시간을 모두 소모하거나, 입출력을 위해 대기해야 하는 경우에 `Context Switching`이 발생한다.
  
  - 프로세스의 상태 변경 : Ready -> Running/ Running -> Ready/ Running -> Waiting

- `Context Switching`은 해당 **OS의 스케줄러**가 우선 순위 알고리즘에 의해 결정, 수행한다. == `Context Switching`을 실행하는 주체는 **OS 스케줄러**이다.

### Context

> 사용자와 다른 사용자, 사용자와 시스템 또는 디바이스간 상호작용에 영향을 미치는 사람, 장소, 개체 등의 현재 상황(상태)을 규정하는 정보들
> 
> OS에서는 CPU가 해당 프로세스를 실행하기 위한 해당 프로세스의 정보들을 의미한다.

- `Context`는 프로세스의 `PCB`에 저장된다.(Metadata와 동일)

### OverHead

- 과부하를 의미한다. 부정적인 의미이지만, 프로세스 작업중 OverHead를 **감수해야 하는 상황**이 있다.
  
  - EX) 프러세스 수행중 인터럽트가 발생하여 Waiting으로 전환. 이때 CPU도 대기하는게 아닌 다른 Waiting 상태의 프로세스를 수행시키는 것이 효율적이다.

### 인터럽트(Interrupt)

- CPU가 프로그램을 실행 중일때, 실행중인 프로그램 밖에서 예외상황이 발생하여 처리가 필요한 경우, CPU에게 알려 예외상황을 처리할 수 있도록 하는 것을 말한다.


- 인터럽트 요청
  
  - I/O request(입출력 요청)
  
  - time slice expired(CPU 사용시간 만료)
  
  - fork a child(자식 프로세스 생성)
  
  - wait for an interrupt(인터럽트 처리를 대기)
  
  - etc...

- 레퍼런스

> [PCB &amp; Context Switching | 👨🏻‍💻 Tech Interview](https://gyoogle.dev/blog/computer-science/operating-system/PCB%20&%20Context%20Switching.html)
> 
> [OS - Context Switch(컨텍스트 스위치)가 무엇인가?](https://jeong-pro.tistory.com/93)
> 
> [운영체제 5: 컨텍스트 스위칭 (Context Switching) :: 머신러닝을 배웠던 데이터 엔지니어](https://hyunie-y.tistory.com/31)
