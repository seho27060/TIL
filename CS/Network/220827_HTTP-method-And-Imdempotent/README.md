- [HTTP method And Imdemponent](#http-method-and-imdemponent)
  - [HTTP method And Imdemponent](#http-method-and-imdemponent-1)
    - [멱등성(Idempotent)](#멱등성idempotent)
    - [HTTP Method의 멱등성](#http-method의-멱등성)
      - [멱등성이 적용되는 Method](#멱등성이-적용되는-method)
        - [GET](#get)
        - [PUT](#put)
        - [DELETE](#delete)
      - [멱등성이 적용되지 않는 Method](#멱등성이-적용되지-않는-method)
        - [POST](#post)
        - [PATCH](#patch)

---

# HTTP method And Imdemponent

## HTTP method And Imdemponent

### 멱등성(Idempotent)

- 수학 및 전산학에서는 같은 연산을 여러번 실행한다고 해도 그 결과가 달라지지 않는 성질을 의미한다.

```java
public int abs(int number) {
    return Math.abs(number);
}
```

- 위 예시를 보면, 같은 함수를 여러번 적용해도 같은 결과값을 반환한다.

- 즉 위 `abs`함수의 반환값을 다시 함수의 파라미터를 전달하더라도 그 결과값이 변화하지 않는다 라는 의미

### HTTP Method의 멱등성

- HTTP Method에서도 동일하게 적용될 수 있다.

#### 멱등성이 적용되는 Method

##### GET

- 서버에서 단순히 읽어오기만 하는 메서드이기 때문에, 당연히 여러번 수행해도 결과가 변화가 없다.

##### PUT

- 서버에 존재하는 리소스를 요청에 담긴 내용대로 통째로 대체해버리므로, 역시 멱등성이 성립한다.

##### DELETE

- 존재하는 데이터를 삭제하는 결과와, 존재하지 않는 결과를 삭제하는 결과에서 응답 코드는 서로 다르겠지만, 서버의 상태 자체는 변하지 않는다.

#### 멱등성이 적용되지 않는 Method

##### POST

- POST 메서드로 서버에 요청시, 요청을 할 때마다 서버에 새로운 데이터가 추가되는 것과 같은 상태가 변화된다. 이는 멱등성에 위배된다.

##### PATCH

- 서버의 리소스를 통째로 대체(replace)하는 `PUT`과는 다르게, 리소스의 일부를 수정하는 `PATCH`메서드는, 사용 전 후에 서버의 상태가 구분되므로 멱등성이 위배된다.

--- 

- 레퍼런스

> 
