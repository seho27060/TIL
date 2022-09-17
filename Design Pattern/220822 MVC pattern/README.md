- [MVC 패턴](#mvc-패턴)
    - [spring MVC 패턴](#spring-mvc-패턴)
# MVC 패턴

- Model - View - Controller

- Model : Controller에서 받은 데이터를 저장

- View : Controlloer로 부터 받은 Model 데이터를 바탕으로 사용자에게 표현

- Controller : 사용자가 접근한 URL에 따라 요청을 파악. URL에 맞는 Method를 호출하여 Servie와 함께 Business Logic 처리

### spring MVC 패턴

![](https://blog.kakaocdn.net/dn/bNgYN8/btqyAMB7FFS/6lxcAlnXqURYkHpP8LyRb1/img.png)

1. Client로부터 요청을 통해 DispatcherServlet 호출

2. DispatcherServlet은 받은 요청을 HandlerMapping에게 전달한다. 요청받은 URL을 분석하여 HandlerMapping 적합한 Controller를 선택하여 반환한다.

3. DispatcherServlet은 HandlerAdapter를 호출하고, HandlerAdapter는 반환받은 Controller에서 요청 URL에 적합한 Method를 찾아준다.

4. Controller는 Business Login을 처리, 해당 결과를 View에 전달할 객체를 Model에 저장한다.

5. Controller는 View name을 DispatcherServlet에게 반환

6. DispatcherServlet은 ViewResolver를 호출, 5.의 View name에 적합한 View를 찾는다.

7. DispatcherServlet은 View 객체에 처리결과를 넘겨 최종 결과를 출력요청

8. View 객체는 해당하는 View를 호출, View는 Model에서 필요한 객체를 가져와 출력하고 Client에게 넘겨준다
