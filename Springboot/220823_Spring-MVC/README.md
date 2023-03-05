# Spring MVC pattern

## Spring MVC

- `Spring`의 전체적인 동작과정은 `MVC pattern`에 기반한다.

- `Dispatcher Servlet`을 중심으로 하여 패턴에서의 역할이 분리되어 문제 발생시 유연한 처리가 가능하다.

### 작동 과정

![](https://media.vlpt.us/images/miscaminos/post/80555c98-2846-4774-9b27-9746336f3dce/springMVC_Dispatcher_centered.jpg)

1. `Spring`에서의 `URL`을 통한 모든 요청은 `DispatcherServlet`으로 향한다.
   
   -  `DispatcherServlet`은 `Front Controller` 역할을 수행한다.

2. `DispatcherServlet`은 `Handler Mapping`을 통해 `URL`에 해당하는 `Controller`를 검색을 요청한다.
   
   - `Handler Mapping`은 요청 `URL`과 매칭되는 `Handler Method`를 반환한다.

3. `DistpatcherServlet`은 `Handler Mapping`의 응답에 기반하여 특정 `Controller`에 `URL` 요청에 대한 처리를 요청한다.
   
   - `Controller` 영역에서는 특정 `Handler Method`에 요청을 전달하며 호출한다.
   
   - `Handler Method`는 적잘한 처리 후 그에 해당하는 `Model`과 `View`를 반환한다.

4. `DispatcherServlet`은 `View Resolver`를 통해 적절한 `View`파일(`/template/view.html`과 같은)을 탐색한다.

5. `DispatcherServlet`은 `View`파일을 `View`에 요청하여 실행한다.
   
   - `View`영역에서는 `View`파일과 요청에 해당하는 `Model`을 사용하여 사용자에게 반환할 페이지를 완성한다.

6. `DispatcherServlet`은 완성된 페이지를 브라우저로 응답하여 사용자에게 전달한다.

### 구성 요소

#### Dispatcher Servlet

> dispatch라는 동작을 수행하며, `HTTP` 프로토콜로 들어오는 모든 요청을 받아 적합한 `Controller`에 위임하는 프론트 컨트롤러(Front Controller)이다.

- `Distpatcher Servlet`의 등장에 따라 요청에 대한 `URL` 매핑을 위한 `web.xml`의 역할이 감소하였다.

- 애플리케이션으로 향하는 모든 요청을 핸들링하며 공동 작업을 처리하여 요청 과정에서의 동작을 간소화한다.

- `MVC pattern`의 측면에서 볼때 `Controller`의 역할을 담당한다.

#### Handler Mapping

> 클라이언트의 `URL` 요청을 어떤 `Controller`가 처리해야할 지 탐색하여 `Distpatcher Servlet`에게 전달한다.

- 실제 `Spring`의 코드상에서 `@RequestMapping`과 같은 어노테이션으로 적절한 `Handler`를 탐색한다.

#### Controller

> 요청에 따른 실질적인 처리를 수행한다. `DispatcherServlet`과 구분되는 백엔드 컨트롤러(Backend Controller)이다.

- `Hadler Mapping`에 따른 특정 `Hadler`(메서드)를 호출하여 실행한다.

- `Model`의 정보를 활용하여 처리를 진행하여 결과를 반환한다.

#### View Resolver

> `Controller`가 반환하는 처리 결과로 생성한 `View`를 결정한다.

- 요청에 따른 적절한 `View`파일을 탐색하여 이를 반환되는 `Model`과 함께 `View` 영역에 전달한다.

---

- 레퍼런스

> [Spring MVC Framework | 👨🏻‍💻 Tech Interview](https://gyoogle.dev/blog/web-knowledge/spring-knowledge/Spring%20MVC.html)
> 
> https://velog.io/@h220101/SpringBoot-%EC%8A%A4%ED%94%84%EB%A7%81-%EB%B6%80%ED%8A%B8-spring-MVC-%ED%8C%A8%ED%84%B4-%EB%8F%99%EC%9E%91
> 
> [[Spring] Dispatcher-Servlet(디스패처 서블릿)이란? 디스패처 서블릿의 개념과 동작 과정 - MangKyu's Diary](https://mangkyu.tistory.com/18)

# 
