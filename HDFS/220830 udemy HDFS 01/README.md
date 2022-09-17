- [udemy HDFS_01](#udemy-hdfs_01)
  - [HDFS(Hadoop distrubuted File System)](#hdfshadoop-distrubuted-file-system)
    - [HDFS Architecture](#hdfs-architecture)
      - [Client Node](#client-node)
      - [Name Node](#name-node)
      - [Data Node](#data-node)
        - [Reading a File](#reading-a-file)
        - [Writing a File](#writing-a-file)
    - [Using HDFS](#using-hdfs)

# udemy HDFS_01

## HDFS(Hadoop distrubuted File System)

- 한개의 디스크 드라이브에 저장하는 기존의 방법에서 여러 컴퓨터에 분산으로 데이터를 저장

- 1블록은 128mb로 한 컴퓨터에는 여러개의 블록으로 구성

- 1개의 디스크에는 여러개의 블록으로 구성

- 특정 데이터는 1개 컴퓨터에 저장되는게 아니라 2개이상의 컴퓨터에 저장된다. 이에 따라 컴퓨터의 물리적 피해에 의한 데이터 소실이 방지할 수 있다.

### HDFS Architecture

#### Client Node

- 애플리케이션이 동작중인 노드

#### Name Node

- 데이터가 어떤 데이터노드에 있는지를 나타내는 정보 와 데이터 이름 및 메타데이터를 저장하는 하나의 노드(디스크)
  
  - 하나의 노드이기 때문에 단일 실패 지점이 발생할 거 같지만, 아래와 같은 예방법이 있다.
    
    1. NFS(network file system)의 로그 기록을 토대로 네임노드를 복구한다.
    
    2. 세컨더리 네임노드(Secondary namenode) 유지, 주 이름 노드의 로그의 복사본을 유지한다.
    
    3. HDFS Federation(HDFS 연합) : 네임노드 볼륨 이라는 서브 디렉터리 마다 네임노드의 데이터 노드 정보를 나눠 갖도록 한다.
    
    4. HDFS high availability : 공유 편집로그 사용.

#### Data Node

- 실제로 데이터가 저장되는 노드. 클라이언트는 네임노드를 통해 찾을려는 데이터의 정보를 얻고, 해당 정보를 토대로 데이터가 존재하는 데이터 노드에 접근한다.

##### Reading a File

1. 클라이언트 노드에서 네임노드에 접근하여 데이터 정보 습득

2. 정보를 토대로 데이터 노드에 접근

##### Writing a File

1. 클라이언트 노드에서 파일을 작성할때, 이름노드에 요청 이름 노드는 저장할 데이터 노드를 지정해줌

2. 클라이언트 노드는 이름 노드에게 지시받은 데이터 노드에 데이터를 저장한다.

3. 저장된 데이터노드는 주위의 다른 데이터 노드에 복사복을 전달하고 또 전달한다.

### Using HDFS

- UI(Ambari)

- Command-Line interface

- HTTP/ HDFS Proxies

- Java interface

- NFS Gateway
