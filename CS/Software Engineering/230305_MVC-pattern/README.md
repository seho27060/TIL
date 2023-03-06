- [MVC Pattern](#mvc-pattern)
  - [MVC](#mvc)
    - [MVC 1](#mvc-1)
    - [MVC 2](#mvc-2)

---

# MVC Pattern

## MVC

> MVC(model-view-controller)는 소프트웨어 공학에서 사용되는 소프트웨어 디자인 패턴으로 사용자 인터페이스로부터 비즈니스 로직을 분리하여 서로간의 영향이 없는 애플리케이션을 구성한다.

- 코드의 재사용을 유용하게 하며, 사용자 인터페이스와 애플리케이션 개발에 필요한 소요 시간을 감축하는 효과적인 설계 방식.
  
  - `MVC 1`과 `MVC 2`가 있다.

- 모델(Model), 뷰(View), 컨트롤러(Controller)의 세 가지의 구성요소를 갖는다.
  
  ![](https://developer.mozilla.org/en-US/docs/Glossary/MVC/model-view-controller-light-blue.png)

- 모델(Model) - 컨트롤러가 받은 요청으로 부터 데이터나 상태를 변경하거나, 상태 변화를 컨트롤러와 뷰에 통보한다. 컨트롤러를 통한 추가/수정/제거의 동작을 하며 상태의 최신 결과를 뷰를 통해 표현한다.
  
  - 애플리케이션 정보, 데이터, DB

- 컨트롤러(Controller) - 요청에 따른 명령을 모델에 전송하여 상태를 변경하거나, 컨트롤러와 관련된 뷰에 명령을 보내어 모델의 상태를 표시한다.
  
  - 데이터와 비즈니스 로직 사이의 상호동작

- 뷰(View) - 사용자가 실제로 보는 결과물을 생성하며, 이를 위해 모델로부터 정보를 얻어온다.
  
  - 사용자가 보는 화면, UI

### MVC 1

| 애플리케이션 구조    |     |                      |     |                  |     |     |
| ------------ | --- | -------------------- | --- | ---------------- | --- | --- |
| User(Client) | ->  | View/Controller(JSP) | <-> | Model(Java Bean) | <-> | DB  |
|              | <-  |                      |     |                  |     |     |

- `JSP` - `View`와 `Controller` 모두를 담당한다.
  
  - 하나의 JSP로 요청, 응답을 처리한다.

- `JSP` 하나로 `MVC`가 모두 구성되어 구현이 쉽지만 그만큼 재사용성과 가독성이 떨어진다.
  
  - 유지보수의 용이성이 떨어진다.

### MVC 2

|              |                  |                     |     |                  |     |     |
| ------------ | ---------------- | ------------------- | --- | ---------------- | --- | --- |
| User(Client) | -><br>(request)  | Controller(Servlet) | ->  | Model(Java Bean) | <-> | DB  |
|              | <-<br>(response) | View(JSP)           | <-> |                  |     |     |

- 모든 요청은 하나의 `Controller`(`Servlet`)가 받는다.

- `Servlet`는 요청에 대해 알맞은 처리 후 그 결과를 `View(JSP)`에 전달한다.

- `MVC 1`과는 다르게 각각의 역할이 분리되어 있어, 문제가 발생할 시 해당 부분만 수정한다.
  
  - 책임에 따른 분리로 유지보수에 용이하다.

---

- 레퍼런스

> [MVC1, MVC2 패턴의 차이점과 Spring MVC 구조 - nickjoIT](https://nickjoit.tistory.com/9)
> 
> https://velog.io/@h220101/SpringBoot-%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B6%80%ED%8A%B8-spring-MVC-%ED%8C%A8%ED%84%B4-%EB%8F%99%EC%9E%91
> 
> [모델-뷰-컨트롤러 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EB%AA%A8%EB%8D%B8-%EB%B7%B0-%EC%BB%A8%ED%8A%B8%EB%A1%A4%EB%9F%AC)
