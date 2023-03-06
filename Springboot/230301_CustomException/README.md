- [CustomException](#customexception)
  - [사용자 정의 예외](#사용자-정의-예외)
    - [Why CustomException?](#why-customexception)
    - [CustomException 적용하기](#customexception-적용하기)
      - [1. ErrorCode 생성](#1-errorcode-생성)
      - [3. ErrorResponseEntity 생성](#3-errorresponseentity-생성)

---

# CustomException

## 사용자 정의 예외

- 함수를 정의하고, 애플리케이션을 통해 `API`를 제공하다 보면 **예외**와 **에러**, **오류**는 의도하지 않던, 의도하던 만나게 된다.
- 3번의 프로젝트를 진행하면서 어려웠던 점이 많이 있었지만, 그 중 디버깅을 위한 로그 확인에 쏟아 부은 시간이 얼마였을까.
  - `Logger`나 `Test`를 통해 충분히 해결 가능하기도 하다.
  - 순전히 서버의 `API`의 "작동"만 추구하는 백엔드는 뭐 딱히 필요 없기도 하겠다. 
- 혼자..라면 이런 삽질은 어찌되든 상관없지만 팀으로 움직일때는 다르다.
  - 보통 `API`의 "작동"만 추구하다 보니, 예외 처리(실패에 대한 처리)가 완전하지 않다.
- 보다 좋은 협업을 위해 필요한게 사용자 정의 예외 아닐까..라고 생각한다.

### Why CustomException?

- `Java`에서는 기본적으로 충분한 예외들을 제공하고 있다. `NPE`, `IllegalArgumentException` 등등.. 

- 하지만 우리가 만든 어플리케이션은 `Java`에 비해 개인적인 프로그램이므로 그에 맞는 예외가 필요하다.
  
  - 즉, 기본 예외들로 **설명되지 않는** 부분들이 있을 수 있다.

- 예외 객체, 요소 등등 모든 내용은 말 그대로 **"사용자 정의"** 이기 때문에 원하는 값들로 예외를 표현할 수 있다.
  
  - 코드,, 이름,, 메시지,, 등등

- 책임에 따른 분리로 메서드들의 응집도가 향상됐다고 할때, 이러한 메서드들의 예외는 하나의 `Java` 기본 예외로 표현된다.
  
  - 각각의 메서드에 따라 상황에 대한 예외를 개발자에게 넘겨줄 수 있다.

- `@ControllerAdvice`를 통해 사용자 정의 예외에 따른 후처리 또한 각각 정의할 수 도 있다.

- `Java`에서 생성되는 기본 예외들은 생각외로 많은 비용을 지출 한다.
  
  - `stack trace`를 통해 `call stack`에 있는 메소드 리스트를 저장한다.
  
  - `Throwable`의 `fillInStackTrace()` 메서드를 `Override`함으로 필요에 따라 `stack trace`의 생성 비용을 줄일 수도 있다.

### CustomException 적용하기

#### 1. ErrorCode 생성

- 예외를 뱉을 때 사용할 `ErrorCode`의 틀을 정의하자. 

- `enum` 을 활용하여 필요한 내용을 미리 정의할 수 있다.

- ```java
  @AllArgsConstructor
  @Getter
  public enum ErrorCode {
  
      /* 404 NOT_FOUND : Resource를 찾을 수 없음 */
      DIARY_NOT_FOUND(HttpStatus.NOT_FOUND, "해당하는 Diary를 찾을 수 없습니다."),
      TAG_NOT_FOUND(HttpStatus.NOT_FOUND, "해당하는 Tag를 찾을 수 없습니다."),
  
      private final HttpStatus httpStatus;
      private final String message;
  }
  ```
  
  `httpStatus`와 `message`를 통해 응답 상태와 메세지를 할당할 수 있도록 했다.

#### 2. CustomException 생성

- `enum` 인 `ErrorCode`를 담을 `class`로 `CustomException`을 생성한다.

- ```java
  @Getter
  @AllArgsConstructor
  public class CustomException extends RuntimeException{
    private final ErrorCode errorCode;
  }
  ```

#### 3. ErrorResponseEntity 생성

- 사용자 정의 예외를 다루는 `CustomExceptionHandler`에서 사용할 `ErrorResponseEntity` 를 정의한다.

- ```java
  @Data
  @Builder
  public class ErrorResponseEntity {
    private int status;
    private String code;
    private String message;
  
    public static ResponseEntity<ErrorResponseEntity> toResponseEntity(ErrorCode e){
        return ResponseEntity
                .status(e.getHttpStatus())
                .body(ErrorResponseEntity.builder()
                        .status(e.getHttpStatus().value())
                        .code(e.name())
                        .message(e.getMessage())
                        .build());
    }
  }
  ```

- 메서드를 통해 `httpStatus`와 `message`에 대한 내용을 `builder` 패턴으로 할당한다.

#### 4. CustomExceptionHandler 생성

- 모든 사용자 정의 예외를 다루는 `CustomHandler`를 생성한다.

- 해당 핸들러는 `Controller` 영역에서 작동하며, 사용자 정의 예외만을 위해 작동한다.

- ```java
  @RestControllerAdvice
  public class CustomExceptionHandler extends ResponseEntityExceptionHandler {
    @ExceptionHandler(CustomException.class)
    protected ResponseEntity<ErrorResponseEntity> handlerCustomException(CustomException e){
        return ErrorResponseEntity.toResponseEntity(e.getErrorCode());
    }
  }
  ```
  
  `Annotation`으로 `ControllerAdvice`, `ExceptionHandler`를 지정해준다.
  
  생성한 `CustomException`을 다루도록 할당한다.
  
  - 여러개의 `CustomException`을 목적에 따라 분류하여 그에 따른 후처리(handling)을 진행해도 된다.

---

- 레퍼런스

> https://velog.io/@dot2__/SpringBoot-Custom-Exception-Response-%EB%A7%8C%EB%93%A4%EA%B8%B0
> 
> https://tecoble.techcourse.co.kr/post/2020-08-17-custom-exception/
> 
> [Spring Exception Handling :: 뱀귤 블로그](https://bcp0109.tistory.com/303)
> 
> [@ControllerAdvice, @ExceptionHandler를 이용한 예외처리 분리, 통합하기(Spring에서 예외 관리하는 방법, 실무에서는 어떻게?)](https://jeong-pro.tistory.com/195)
