[TOC]

# Java_07

## 객체지향 프로그래밍 II

#### 상속

- 상속 : 기존의 클래스를 재사용하여 새로운 클래스를 작성하는 것

```java
class Parent {}
class Child extends Parent {
    // ...
}
```

- 상속받고자 하는 클래스의 이름을 키워드 `extends`와 함께 써주면 된다.

- 자손 클래스는 조상 클래스의 모든 멤버를 상속받는다.( 생성자와 초기화 블럭은 제외)

- 자손 클래스의 멤버 개수는 조상 클래스도바 항상 같거나 많다.

### 클래스 간의 관계 - 포함관계

- 클래스간의 관계를 맺는데 상속만 있는게 아니다.

- 포함(composite)를 통해 한 클래스의 맴버변수로 다른 클래스 타입의 참조변수를 선언할 수 있다.

```java
class Point {
    int x;
    int y;
}
class Circle {
    Point c = new Point(); // 포함을 통해 다른 클래스를 멤버변수로 추가
    int r;
}
```

#### 클래스 간의 관계 결정하기

- 클래스를 작성하는데 **상속**관계가 좋을까 **포함**관계가 좋을까

> 원(circle)은 점(point)이다. - 상속
> 
> 원(circle)은 점(point)를 가지고 있다. - 포함

#### 단일 상속(single inheritance)

- Java에서는 1개의 조상 클래스만을 갖는 단일 상속만이 가능하다.

#### Object 클래스 - 모든 클래스의 조상

- 클래스를 선언할때 컴파일러는 자동으로 `extends Object`를 추가한다.

- 이를 통해 모든 클래스는 `Object`를 조상 클래스로 갖게 된다.

#### 오버라이딩(overriding)

- 조상 클래스로부터 상속받은 메서드의 내용을 변경하는 것.

- 오버라이딩의 조건
  
  1. 선언부가 조상 클래스의 메서드와 일치해야 한다.
  
  2. 접근 제어자를 조상 클래스의 메서드보다 좁은 범위로 변경할 수 없다.(접근 제어자 : public, protected, (default), private)
  
  3. 예외는 조상 클래스의 메서드보다 많이 선언할 수 있다.

#### 오버로딩 vs. 오버라이딩

- 오버로딩(overloading) : 기존에 없는 새로운 메서드를 정의하는 것.

- 오버라이딩(overriding) : 상속받은 메서드의 내용을 변경하는 것.

```java
class Parent {
    void parentMethod() {}
}

class Child extends Parent {
    void parentMethod() {} // 오버라이딩
    void parentMethod(int i) {} / 오버로딩

    void childMethod() {}
    void childMethod(int i) {} // 오버로딩
    void childMethod() {}
}
```

#### 참조변수 super

- `super`는 자손 클래스에서 조상 클래스로부터 상속받은 멤버를 참조하는데 사용되는 참조변수이다. 

- 멤버변수와 지역변수의 이름이 같을 때 `this`를 붙여 구별했듯이, 상속받은 멤버와 자신의 멤버와 이름이 같을때 `super`를 붙여서 구별할 수 있다.

#### super() - 조상의 생성자

- `this()`와 같이 `super()`도 생성자이다. `this()`는 같은 클래스의 다른 생성자를 호출하는데 사용되지만, `super()`는 조상의 생성자를 호출하는데 사용된다.

```java
Point3D(int x, int y, int z) {
    super(x,y); // 조상클래스의 생성자 Point(int x, inty) 를 호출
    this.z = z; // 자신의 멤버를 초기화
}
```

#### import 문

- 이클립스에서 단축키 `ctrl + shift + o`를 누르면 자동으로 import 문을 추가해준다.

```java
import 패키지명.클래스명;
import 패키지명.*;
```

#### static import 문

- `static import`문을 사용하면 static 멤버를 호출할 때 클래스 이름을 생략할 수 있다.

```java
import static java.lang.Integer.*; // Integer클래스의 모든 static 메서드
import static java.lang.Math.random; // Math.random()만, 괄호 안붙임.
import static java.lang.System.out; // System.out을 out만으로 참조가능
```

### 제어자(modifier)

- 제어자는 클래스, 변수 또는 메서드의 선언부에 함께 사용되어 부가적인 의미를 부여한다.

- 접근 제어자 : public, protected, (default), private

- 그 외 : static. final, abstract, native, transient 등등

- 하나의 대상에 여러 제어자를 조합하여 사용 가능하나, 접근제어자는 1개만 선택하여 사용한다.

#### static - 클래스의, 공통적인

- 인스턴스 멤버를 사용하지 않는 메서드를 static을 붙여서 static 메서드로 선언하는 것을 고려해보도록 하자.

- 멤버변수, 메서드, 초기화 블럭에 사용가능

#### final - 마지막의, 변경될 수 없는

- 사용되면 이후에 수정, 오버라이딩이 불가함

- 클래스, 메서드, 멤버변수, 지역변수 에 사용가능

#### abstract - 추상의, 미완성의

- 메서드의 선언부만 작성하고 실제 수행내용은 구현하지 않은 추상 메서드를 선언하는데 사용된다.

- 클래스, 메서드에 사용가능

#### 접근 제어자(access modifier)

- private : 같은 클래스 내에서만 접근이 가능하다

- (default) : 같은 패키지 내에서만 접근이 가능하다

- protected : 같은 패키지 내에서, 그리고 다른 패키지의 자손클래스에서 접근이 가능하다.

- public : 접근 제한이 전혀 없다.

#### 캡슐화와 접근 제어자

- 접근 제어자를 사용하는 이유는 클래스의 내부에 선언된 데이터를 보호하기 위해서이다.

- 이것을 데이터 감추기(data hiding)라고 하며, 객체지향개념의 캡슐화(encapsulation)에 해당한다.

- 클래스 선언에 있어서 getter, setter에 따라 적절한 접근 제어자를 할당해주도록 하자.

### 다형성(polymorphism)

- 여러 가지 형태를 가질 수 있는 능력

- 자바에서는 한 타입의 참조변수로 여러 타입의 객체를 참조할 수 있도록 함으로서 다형성을 구현

```java
class Tv {
    boolean power;
    int channel;

    void power() { power = !power;}
    void channelUp() { ++channel;}
    void channelDown() { --channel;}
}

class SmartTv extends Tv {
    String text;
    void caption() {}
}
```

```java
SmartTv s = new SmartTv(); // 참조 변수와 인스턴스 타입이 일치
Tv t = new SmartTv(); // 조상 타입 참조변수로 자손 타입 인스턴스 참조
```

- 조상타입의 참조변수로 자손타입의 인스턴스를 참조할 수 있다.

- 반대로 자손타입의 참조변수로 조상타입의 인스턴스를 참조할 수 는 없다.

#### 참조변수의 형변환

- 서로 상속관계에 있는 타입간의 형변환은 양방향으로 자유롭게 수행 가능하다.

- 참조 변수가 가리키는 인스턴스의 자손타입으로 형변환은 허용되지 않는다.

#### instanceof 연산자

- 참조변수가 참조하고 있는 인스턴의 실제 타입을 알아보기 위해 사용.

```java
void doWork(Car c) {
    if (c instanceof FireEngine){ // 1. 형변환이 가능한지 확인
        FireEngine fe = (FireEngine)c; // 2. 형변환
        fe.water();
}
}
```

- 어떤 타입에 대한 `instanceof`연산의 결과가 true라는 것은, 검사한 타입으로 형변환이 가능하다는 것을 뜻한다.

#### 매개변수의 다형성

- 참조변수의 다형적인 특징은 메서드의 매개변수에도 적용된다.

- 메서드의 매개변수가 어떤 조상클래스인 경우. 해당 조상클래스의 자손타입의 참조변수면 어느 것이나 매개변수로 받아들일 수 있다.

#### 여러 종류의 객체를 배열로 다루기

```java
Product p[] = new Product[3];
p[0] = new Tv();
p[1] = new Computer();
p[2] = new Audio();
```

- 이와 같이 조상타입의 참조변수 배열을 사용하여, 공통의 조상을 가진 서로 다른 종류의 객체를 배열로 묶어서 다룰 수 있다.

- `Vector`클래스를 사용하면, 배열에 객체를 추가, 제거하면 배열의 크기를 알아서 관리해준다.

### 추상

#### 추상 클래스(abstract class)

- '미완성 설계도'라고 할수 있다. 추상클래스로는 인스턴스를 생성할 수 없고, 상속을 통한 자손클래스에 의해서만 완성가능하다.

```java
abstract class 클래스이름{
    ...
}
```

#### 추상 메서드(abstract method)

- 설계만 해놓고 실제 수행 내용은 작성하지 않은 미완성 메서드.

- 상속받는 클래스마다 메서드의 내용이 달라질 수 있기 때문에, 내용을 비워놓는다.

```java
abstract 리턴타입 메서드이름();
///
abstract class Player{
    abstract void play(int pos);
    abstract void stop(); // 2개의 추상 메서드
}

class AudioPlayer extends Player{
    void play(int pos){ // 실행내용}; 
    void stop() { // 실행내용}; // 2개의 추상메서드를 구현
}
```

#### 추상클래스의 작성

- 추상화 : 기존의 클래스의 공통부분을 뽑아내서 조상 클래스를 만드는 것 <-> 구체화

- 상위 클래스로 갈수록 추상화가 되고, 하위 클래스로 갈수록 구체화된다.

### 인터페이스(interface)

- 추상 메서드와 상수만을 멤버로 가지는 일종의 추상 클래스

- 다른 클래스를 작성하는데 도움 줄 목적으로 작성된다.

- 접근 제어자로 public, default 만 사용가능

```java
interface 인터페이스이름{
    public static final 타입 상수이름 = 값;
    public abstract 메서드이름(매개변수목록);
}
```

- 인터페이스는 인터페이스로부터만 상속이 가능하다(다중 상속가능)

#### 인터페이스의 구현

- 그 자체로 사용 불가하며, 상속을 통해 구현이 이뤄진다.

- 상속(확장)을 의미하는 `extends`와 구분되게 구현한다는 의미로 `implements`가 사용된다.

```java
class 클래스이름 implements 인터페이스이름 {
    // 인터페이스에 정의된 추상메서드를 모두 구현해야한다.
}
class Fighter implements Fightable{
    public void move(int x, int y){ // 실행내용}
    public void attack(Unit u) { // 실행내용}
}
```

- `Fighter`클래스는 `Fightable`인터페이스로 구현한다.

#### 인터페이스를 이용한 다형성

- 인터페이스 타입의 참조변수로 이를 구현한 클래스의 인스턴스에 참조할 수 있다.

- **리턴타입이 인터페이스라는 것은 메서드가 해당 인터페이스를 구현한 클래스의 인스턴스를 반환한다는 것을 의미한다.**(인터페이스는 추상클래스이므로, 구현된 하위 클래스를 반환한다.)

#### 인터페이스의 장점

1. 개발시간을 단축시킬 수 있다.

2. 표준화가 가능하다.

3. 서로 관계없는 클래스들에게 관계를 맺어 줄 수 있다.

4. 독립적인 프로그래밍이 가능하다.

#### 디폴트 메서드와 static 메서드

- 이미 인터페이스를 구현한 클래스가 존재할때, 인터페이스에 새로운 추상 메서드를 추가하면 하위 클래스들 모두에 새롭게 구현을 정의해야한다.

- 이러한 비효율적 구현을 피하기 위해 **디폴트 메서드(default method)** 을 사용한다.

- 추상 메서드가 아니기때문에 하위 클래스에 모두 구현하지 않아도 된다.

```java
interface MyInterface {
    void method();
    void newMethod(); // 추상메서드
}

///
interface MyInterface {
    void method();
    default void newMethod(){} // 디폴트 메서드 추가.
}
```

### 내부 클래스(inner class)

- 클래스 내에 선언된 클래스.

- 내부 클래스 종류
  
  - 인스턴스 클래스
  
  - 스태틱 클래스
  
  - 지역 클래스
  
  - 익명 클래스

```java
class Outer{
    private class InstanceInner{}
    protected static class StaticInner {}

    void myMethod() {
       class LocalInner{}
    }
}
```
