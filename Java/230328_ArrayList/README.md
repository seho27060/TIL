[TOC]

# ArrayList

## ArrayList

- 파이썬에서는 배열을 생성하면 자동으로 동적 배열(Dynamic Array)로 생성이 되지만,

- 자바에서는 그러지 않아서.. 있을법도 한데 몰라서 찾아봤다.

- `ArrayList`를 활용하면 크기가 동적인 배열을 생성할 수 있고
  
  - `Stream`과 같은 `API`로 다양한 집계도 가능하다.

- `List` 인터페이스를 클래스가 `ArrayList`이고 `Queue`, `Set`을 구현한 클래스도 있고 다양하다.

### 사용 예시

```java
ArrayList<Integer> arrList = new ArrayList<>();
```

- 위와 같이 `ArrayList<참조타입> 변수이름 = new ArrayList<>();`로 객체를 생성하여 동적 배열을 다룰 수 있다.

- `add`, `remove`, `get`, `size` 등과 같이 배열을 조작하거나 조회할 수 있는 다양한 메서드를 지원한다.

---

- 레퍼런스

> [Java - 동적배열[ArrayList](8)](https://what-am-i.tistory.com/63?category=1000403)
