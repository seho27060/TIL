- [springboot_00](#springboot_00)
  - [Spring vs. SpringBoot](#spring-vs-springboot)
      - [spring boot 시작하기](#spring-boot-시작하기)
      - [작업 파일](#작업-파일)
      - [작업 폴더](#작업-폴더)
# springboot_00

## Spring vs. SpringBoot

- spring vs springboot 

- springboot : 버전관리해줌

#### spring boot 시작하기

- springboot initializer : 설정에 맞는 압축파일을 줌  

![2022-08-22-16-39-46-image.png](https://github.com/seho27060/TIL/blob/8ad96db3ef58f58e9382d60aa248cdcaa0cebde2/Springboot/220822%20springboot%2000/images/2022-08-22-16-39-31-image.png)

- project 
  
  - maven : xml를 사용 문서화 성격강함
  
  - gradle : 거의 대부분 요즘 이거씀 

![2022-08-22-16-39-31-image.png](https://github.com/seho27060/TIL/blob/8ad96db3ef58f58e9382d60aa248cdcaa0cebde2/Springboot/220822%20springboot%2000/images/2022-08-22-16-39-46-image.png)

![2022-08-22-16-43-36-image.png](https://github.com/seho27060/TIL/blob/8ad96db3ef58f58e9382d60aa248cdcaa0cebde2/Springboot/220822%20springboot%2000/images/2022-08-22-16-43-36-image.png)

위 종속성을 기본으로 갖는 스프링압축파일 생성

#### 작업 파일

- build.gradle : 플러그인 설정파일

#### 작업 폴더

- controller - api 관련 코드

- domain

- repository - db와 관련된 코드

- service - 실제 api에 대한 역할을 맡아줌

![2022-08-22-19-36-55-image.png](https://github.com/seho27060/TIL/blob/8ad96db3ef58f58e9382d60aa248cdcaa0cebde2/Springboot/220822%20springboot%2000/images/2022-08-22-19-36-55-image.png)

controller : 요청이 어디로 왔고, 무엇을 원하는지, 원하는걸 반환해주면 됨

- service : controller에서 service를 호출, controller의 어떻게를 수행(요청 동작 수행)

- repository : 가장 단순한 도구 모음. db에 접근하는 쿼리 모음/service가 데이터를 가지고 복잡한 일을 할때, 해당 데이터에 관련된 crud를 담당함.

- 추상화를 통한 유지보수, 개발의 용이성 증대

