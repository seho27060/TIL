# JavaScript_04
## JavaScript AJAX
[toc]

### AJAX, axios(promise)
#### 구동과정. 

- js_06_workshop_practice 토대로 작성
- template, view를 장고로 구현한 pjt는 동기적 구성의 웹 == 새로고침으로 화면 전환이 일어난다.
- AjAX를 이용하여 비동기적(현재상태 그대로의, 새로고침이 없는) 화면전환을 구성하기.



- django로 구성된 기본 view, template에서 AJAX의 종류인 axios를 활용한다.
  - template의 요청은 axios가 대체하게 된다.
  - django를 통해 구현했던 기능들을 js를 통해 비동기적으로 구현 가능하다.
  - 필요한 정보를 view에서 구현하고, html상의 script에서 필요한 프레임워크의 cdn을 주고 기능 구현.

