- [Today's Keyword\_01](#todays-keyword_01)
  - [Java](#java)
    - [Optional](#optional)
      - [orElse와 orElseGet](#orelse와-orelseget)
      - [Optional 사용법 가이드](#optional-사용법-가이드)
    - [Lambda](#lambda)
      - [Lambda Expression](#lambda-expression)
      - [detail-index1](#detail-index1)
# Today's Keyword_01

## Java

### Optional

- 개발할 때 가장 많이 발생하는 예외 중 하나인 **NPE**. **NPE**를 예방하기 위해서 사용하는 객체의 null 검사를 해야한다. 

> `Optional`은 null을 반환하면 오류가 발생할 가능성이 매우 놓은 경우에 '결과 없음'을 명확하게 명시하기 위해 메서드의 반환 타입으로 사용되도록 매우 제한적인 경우로 설계되었다. - Brian Goetz(Java 설계자)

- `Optional`의 **정의에 기반**하여 **사용방법을 준수**하지 않고 남용할 경우. **불필요한 비용 소모와 많은 부작용**이 발생할 수 있다.

```java
TestObject testObject = TestMethod(); // 반환값이 null일 수 도 있는 어떤 함수 TestMethod 

System.out.println(testObject.toString()); // testObject가 null인 경우 NPE 발

if(testObject != null){
    System.out.println(testObject.toString()); // null인지 확인하는 작업 후 변수를 호출해야함.
} else{
    System.out.println("this object is null");
}

//----------------------

Object<TestObject> testObject = Optional.OfNullable(TestMethod()).orElse(System.out.prinln("this object is null"));
```

- 위와 같은 상황에서 `Optional` 클래스를 사용한다면 훨씬 명시적이고 간결한 코드를 작성할 수 있다.
- `Optional<T>` : `null`이 올 수 있는 값을 감싸는 `wrapper` 클래스로, `null`일 수 있는 값을 참조하더라도 NPE가 발생하지 않도록 도와준다.

#### orElse와 orElseGet

- Optional API의 단말 연산에는 orElse와 orElseGet 함수가 있다. 

- `orElse` : 파라미터로 값을 받는다.

- `orElseGet` : 파라미터로 함수형 인터페이스(함수)를 받는다.

```java
public void Change() {
    String result = "Result";
    System.out.println("change to Result");
    return result;
}

String test = "test";

Object<TestObject> testObject = Optional.OfNullable(test)
    .orElse(Change());
System.out.println(testObject);
// change to Result
// test
// 가 출력된다.
Object<TestObject> testObject = Optional.OfNullable(test)
    .orElseGet(Change());
// test
// 가 출력된다.
```

- `orElse`의 경우 파라미터의 값이 함수일 경우 **일단 호출**되지만
  - 하지만 `testObject`의 값이 null이 아니므로 여전히 "test"이다.
- `orElseGet`의 경우 `testObject`의 값이 null인 경우 호출된다.
  - 호출되지도 않았으니 `testObject`는 여전히 "test"이다.

#### Optional 사용법 가이드

- `Optional`변수에 `Null`을 할당하지 않는다.
  
  ```java
  publci Optional<testResult> testMethod() {
  
  ...
  
  Optional<testResult> emptyResult = null; 
  // Optional의 입장에서는 emptyResult가 어떤 값인지 모르니, 확인한 후 null임을 인지한다.
  
  Optional<testResult> emptyResult = Optional.empty(); 
  // 이와 같이 Optional.empty()를 통해 빈 값을 할당해주자.
  }
  ```

- 값이 없을 때 `Optional.orElseX()`로 기본 값을 반환하라.
  
  ```java
  public String returnDefault(){
  return "default";
  }
    public String testMethod(){
    Optional<String> optionalResult = ...;
  
    // 적용 전
    // optionalResult의 값이 null인지 확인후 반환한다.
    if(optionalResult.isPresent()){
        return optionalResult.get();
    } else {
        return returnDefault();
    }
  
    // 적용 후
    return optionalResult.orElseGet(returnDefault());
    }
  ```

- 단순히 값을 얻으려는 목적으로만 `Optional`을 사용하지 않는다.

- 생성자, 수정자, 메서드 파라미터 등으로 `Optional`을 넘거지 않는다.
  
  ```java
  public void TestMethod(Optional<String> input){
  // Optional인 input을 다시 null 확인을 하고 반환하는.. 상당히 비효율적이다.
  return Optional.ofNullable(input);
  }
  ```

- `Collection`의 경우 `Optional`이 아닌 빈 `Collection`을 사용한다.

- 반환 타입으로만 사용하라

### Lambda

#### Lambda Expression

> 함수를 하나의 식(Expression)으로 표현함.
> 
> 프로그래밍 언어에서 사용되는 개념으로 익명 함수(Anonymous Function)를 지칭하는 용어.

#### detail-index1

---

---

- 레퍼런스

> [[Java] Optional이란? Optional 개념 및 사용법 - (1/2) - MangKyu's Diary](https://mangkyu.tistory.com/70)
> 
> [[Java] 언제 Optional을 사용해야 하는가? 올바른 Optional 사용법 가이드 - (2/2) - MangKyu's Diary](https://mangkyu.tistory.com/203)
