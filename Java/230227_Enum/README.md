- [Java](#java)
  - [Enum](#enum)
      - [특징](#특징)
    - [`Enum` 생성하기](#enum-생성하기)

---

# Java

## Enum

> 한정된 데이터만을 가지는 자료형으로 **"Enumeration Type"** 이라는 뜻

- `Java 1.5` 부터 `Enum`과 같은 "열거형 타입"을 사용할 수 있게 되었다.

- `Enum` 타입을 선언하기 위해 `Class`명에 첫 글자를 대문자로 하거나,
  
  - `class` 대신 `enum`을 적거나
  
  - 요소를 상수로 적을때는 대문자로 적거나
  
  - 상수가 2개 단어로 연결되면 `"\_"로 연결하는 것과 같은 관례가 있다.

- 자주 사용해야하나 한정된 데이터로 이뤄진 값들을 `Enum`을 통해 묶어서 사용할 수 있다.

#### 특징

- 선언된 `enum`은 메모리의 `Heap` 영역에 저장된다.
  
  - 이후에 생성되는 `enum` 인스턴스 들은 동일한 `Heap` 영역의 `enum` 객체를 바라본다.

- 모든 `enum` 인스턴스들은 `java.lang.Enum` 클래스를 상속받으므로, `name()`, `ordinal()`, `compareTo()`, `valueOf(String name)`, `values()` 메서드를 사용할 수 있다.

### `Enum` 생성하기

- `Enum` 클래스 생성하기
  
  ```java
  public enum Day {
      MON, TUE, WED, THU, FRI, SAT, SUN
  }
  ```
  
  위와 같이 간단하게 생성할 수 있다.

- ```java
  public enum Day{
      MON("Monday"),
      TUE("Tuesday"),
      WED("Wednesday"),
      THU("Thusday"),
      FRI("Friday"), 
      SAT("Saturday"),
      SUN("Sunday");
  
      private final String label;
  
      Day(String label) {
          this.label = label;
      }
  
      public String label(){
          return label;
      }
  }
  ```
  
  필드값을 추가하면서 생성자도 같이 추가했다.
  생성자가 있다고 해서 `new`로 `enum` 객체를 생성할 수 없다.

- ```java
  System.out.println(Day.MON.name()); // MON 출력
  System.out.println(Day.MON.label()); // Monday 출력
  ```

- 이외로 `MON("Monday", 0)`과 같이 필드값에 여러 개의 값을 연결할 수도 있다.

---

- 레퍼런스

> [Java Enum이란 | 기록하는 개발자](https://honbabzone.com/java/java-enum/)
> [[Java Enum 1편 : Enum 기본적인 사용 :: 뱀귤 블로그](https://bcp0109.tistory.com/334)
