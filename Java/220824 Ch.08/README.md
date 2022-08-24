[TOC]

# Java_08

## 예외처리

### 프로그램 오류

- 오류에는 컴파일에러, 런타임에러, 논리적에러 가 있다.

- 프로그램의 실행도중 발생하는 런타임 에러에 대한 대비로 **예외처리**을 사용한다.

- 자바에서는 프로그램 오류를 "에러(error)"와 "예외(exeption)", 두 가지로 구분하였다.

### 예외 클래스의 계층구조

- 자바에서는 실행 시 발생할 수 있는 오류(Exception, Error)를 클래스로 정의하였다.

- Object
  
  - Throwable
    
    - Exception
      
      - RuntimeException
      
      - ...
      
      - IOException
    
    - Error
      
      - OutOfMemoryError
      
      - ...

### Exception과 RuntimeException

- Exception클래스들 : 사용자의 실수와 같은 외적인 요인에 의해 발생하는 예외

- RuntimeException클래스들 : 프로그래머의 실수로 발생하는 예외

### 예외 처리하기 - try-catch문

- 예외처리(Exception Handling) : 프로그램 실행 시 발생 할 수 있는 예기치 못한 예외의 발생에 대비한 코드를 작성. 프로그램의 비정상 종료를 막고, 정상적인 실행상태를 유지한다.

```java
try{
    // 예외 발생 가능한 문장을 입력
} catch (Exception1 e1){
    // Exception1이 발생했을때, 처리 코드 입력
} catch (Exception2 e2){
    // Exception2이 발생했을때, 처리 코드 입력
}
```

#### 예외의 발생과 catch블럭

- catch블럭은 괄호()와 블럭{} 두 부분으로 나눠져 있다. 
- 괄호내에는 처리하고자 하는 예외와 같은 타입의 참조변수를 선언한다
  - 예외 발생시, 발생한 예외에 해당하는 클래스의 인스턴스가 생성된다.
  - 모든 예외 클래스는 Exception클래스의 자손이므로, Exception 클래스 타입으로 참조변수를 선언하면 여러 종류의 예외가 발생하더라도 해당 catch블럭에 의해 처리된다.

#### printStackTrace()와 getMessage()
- 예외 발생시 생성되는 예외 클래스의 인스턴스에는 printStackTrace()와 getMessage()를 통해 예외 정보를 확인할 수 있다.

#### 멀티 catch 블럭
- 다수의 catch 블럭을 '|' 기호를 통해 하나의 catch 블럭으로 합칠 수 있다.
```java
try {
	...
} catch (ExceptionA a) {
	a.printStackTrace()
} catch (ExceptionB b) {
	b.printStackTrace()
}
///
try {
	...
} catch (ExceptionA | ExceptionB e) {
	e.printStackTrace()
}
```

#### 예외 발생시키기
- `throw`키워드를 통해 프로그래머가 고의로 예외를 발생시킬 숭 ㅣㅆ다.
```java
try {
	Exception e = new Exception("고의로 발생 시킴"); // 사용자 정의 예외 생성
    throw e; // 예외를 고의로 발생
} catch( Exception e) {
	e.printStackTrace();
}
```

### 메서드에 예외 선언하기
- 예외를 처리하는 방법으로 `try-catch`문뿐만 아니라, 예외를 메서드에 선언하는 방법이 있다.
- `throws`키워드를 통해 메서드 내에서 발생 가능한 예외를 명시해준다.

```java
void method() throws Exception1, Exception2, ...{
	// 메서드 내용
}
```
- 메서드의 선언부에 예외를 선언함으로 메서드를 사용하려는 사람이 해당 메서드에 어떤 예외를 처리해야 하는지 쉽게 알 수 있다.

### finally 블럭
- 예외의 발생여부에 상관없이 실행되어야할 코드를 포함시킬 목적으로 사용된다.
- `try-catch`문의 끝에 선택적으로 덧붙여 사용된다.

```java
try {
	// try 실행내용
} catch (Exception e1) {
	// 예외처리
} finally {
	// 예외와 관계없이 항상 수행되는 구문
}
```

### 예외 되던지기(exception re-throwing)
- 한 메서드에서 발생 가능한 예외가 여럿인 경우, 몇 개는 `try-catch`문을 통해 메서드 자체적으로 처리하고, 그 나머지는 선언부에 지정하여 호출한 메서드에서 처리하도록 함으로 양쪽에서 나눠 처리할 수 있다.
- 또한 예외가 발생한 메서드와, 해당 메서드를 호출한 메서드 양쪽에서도 처리가 가능하다.
