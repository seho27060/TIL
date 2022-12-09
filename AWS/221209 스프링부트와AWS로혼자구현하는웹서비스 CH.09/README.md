[TOC]

# Springboot and AWS_04

## CH.09 Travis CI 배포 자동화

- 여러 개발자의 코드가 실시간으로 병합되고, 테스트가 수행되고, master브랜치의 푸시에 배포가 자동으로 이뤄지는 환경을 구성해보자.

- CI(Continuous Integration, 지속적 통합) : 코드 버전 관리(git)에 push되면 **자동**으로 **테스트와 빌드가 수행**되어 안정적인 배포 파일을 만드는 과정

- CD(Continuous Deployment,  지속적 배포) : 빌드 결과를 자동으로 운영 서버에 무중단 배포가 진행되는 과정

#### 1. Travis CI 연동하기

- Travis CI : github에서 제공하는 무료 CI 서비스

- Travis CI 웹 서비스 설정
  
  - 20년 이후로 결제 정보를 등록해야 한다. 결제 카드의 해외결제차단 서비스를 풀어야 결제가 된다^^;;

- 프로젝트 설정
  
  - .travis.yml 파일로 상세 설정 진행
  
  - YAML(야믈) : JSON에서 괄호를 제거한 형태로, 기계에서 파싱이 쉽고 사람이 다루기 쉬운 확장자

- Travis CI의 대쉬보드에서 커밋내역에 따른 CI가 성공함을 확인 가능 하다.

#### 2. Travis CI와 AWS S3 연동하기

- **AWS S3**(Simple Storage Service) : AWS에서 제공하는 일종의 파일 서버. 정적 파일과 배포 파일을 관리 가능하며 보통 이미지 업로드를 구현할때 사용한다.
1. Travis CI와 S3 연동
   
   - AWS CodeDeploy 서비스를 사용한다. S3 연동에 필요한 Jar 파일을 전달한다.
   
   - Travis CI가 빌드한 결과물을 받아서 CodeDeploy가 가져갈 수 있도록 보관하는 공간으로 S3를 사용한다.

2. AWS Key 발급
   
   - 일반적으로 AWS 서비스에 외부 서비스는 접근 할 수 없다.
   
   - 접근 권한을 갖는 Key를 생성하여 사용해야 한다.
   
   - IAM(Identity and Access Management)로 서비스의 접근 방식과 권한을 관리한다.

3. Travis CI에 키 등록
   
   - 설정화면에서 환경변수로 access key와 secret key를 등록한다.
   
   - 등록한 값은 `.travis.yml`에서 사용할 수 있다.

4. S3 버킷 생성
   
   - 파일을 저장하고 접근 권한을 관리, 검색 등을 지원하는 파일 서버의 역할
   
   - Travis CI에서 생성된 Build 파일을 저장하도록 한다.
   
   - 저장된 Build 파일은 이후 AWS의 CodeDeploy에서 배포할 파일로 가져가도록 구성한다.
   
   - 보안과 권한 설정은 IAM사용자로 발급받은 키로 접근 가능하므로, 퍼블릭 액세스를 차단한다.

#### 3. Travis CI와 AWS S3, CodeDeploy 연동하기

- AWS의 배포 시스템인 CodeDeploy를 사용해보자
1. EC2에 IAM 역할 추가하기
   
   - 역할 : AWS 서비스에서만 할당할 수 있는 권한/ 사용자 : AWS 서비스 외에 사용할 수 있는 권한
   
   - CodeDeploy를 사용하므로 역할을 생성한다.
   
   - EC2 인스턴스에 생성한 역할을 정책에 추가한다.

2. CodeDeploy 에이전트 설치
   
   - EC2  서버에 CodeDeploy 에이전트를 설치한다.
   
   - 실행에 필요한 권한을 부여후 실행 확인

3. CodeDeploy를 위한 권한 생성
   
   - CodeDeploy에서 EC2 서버에 접근하기 위한 권한이 필요하다.
   
   - AWS 서비스(CodeDeploy)에서 접근하므로 **역할**을 생성한다.

4. CodeDeploy 생성
   
   - AWS의 배포 서비스인 code Commit 과 code Build는 각각 github와 jenkins로 대체된다.
   
   - CodeDeploy는 **대체재가 없으므로** 생성이 필요하다. 

5. Travis CI, S3, CodeDeploy 연동
   
   - S3에서 넘겨줄 zip 파일을 저장할 디렉토리를 EC2 서버에 생성한다.
   
   - AWS CodeDeploy를 설정한 `appspec.yml`을 프로젝트에 생성한다.
   
   - `.travis.yml`파일에도 CodeDeploy 설정 내용을 추가한다.
   
   - 저장소에 푸쉬하면 연동 완료!

#### 4. 배포 자동화 구성

- Travis CI, S3, CodeDeploy 들을 연동했다. 이를 기반으로 Jar를 배포하여 실행해보자.

- EC2 서버의 `step2`에서 실행 될 `deploy.sh`파일을 프로젝트에 추가

- `.travis.yml` 파일 수정
  
  - 현재는 프로젝트의 모든 파일을 zip 파일로 만든다.
  
  - 배포에 실제로 필요한 파일은 `Jar`, `appsepc.yml`, `배포를 위한 스크립트`이므로 해당 파일들만 zip으로 만들도록 `.travis.yml`파일을 수정한다.
  
  - 아 ㅋㅋ &를 %로 써서 계속 배포가 안됨 ㅋㅋ
    
    - 오류나면 로그를 확인해보자!!!

- `appspec.yml` 파일 수정
  
  - 배포에 필요한 `deploy.sh` 파일로 애플리케이션을 시작하도록 수정한다.

- AWS 보안 그룹에서 배포 서비스의 포트가 열려있는지 확인한다.

- 사용하는 소셜 로그인 클라우드 플랫폼에 AWS EC2 서버의 퍼블릭 DNS를 등록한다.

---

- 레퍼런스

> 스프링 부트와 AWS로 혼자 구현하는 웹 서비스
