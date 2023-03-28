# Operator

## 연산자

#### 형변환 연산자

- 형변환 : 변수나 리터럴의 타입을 다른 타입으로 변환하는 것(casting)

```java
double d = 85.4;
int score = (int)d; // 85로 변환되어 출력.
```

| 변환           | 수식        | 결과    |
| ------------ | --------- | ----- |
| int -> char  | (char)65  | 'A'   |
| char -> int  | (int)'A'  | 65    |
| float -> int | (int)1.6f | 1     |
| int -> float | (float)10 | 10.0f |

#### 자동 형변환

- 컴파일러는 **"기존의 값을 최대한 보존할 수 있는 타입으로 자동 형변환한다"**

- 보통 표현범위가 좁은 타입 -> 표현범위가 넓은 타입 으로 형변환된다.
  
  - `byte` -> `short`,`char` -> `int` -> `long` -> `float` -> `double` 와 같다.

#### 산술 변환

- 이항 연산자는 두 피연산자의 타입이 일치해야 연산이 가능하다.

- 피연산자의 타입의 일치를 위해 자동 형변환되는 것을 '산술 변환'이라고 한다.
  
  - 보통 큰 타입으로 일치시킴

```java
class ex {
    public static void main(String[] args) {
        byte a = 10;
        byte b = 30;
        byte c = (byte)(a*b); // 연산된 큰 자료형의 값을 작은 값의 자료형으로 명시적으로 변환해줌.
        System.out.println(c);
    }
}
```

- 크기가 작은 자료형의 변수를 큰 자료형의 변수에 저장할 때는 자동으로 형변환(type conversion, casting)되지만, 반대로 큰 자료형의 값을 작은 자료형의 변수에 저장하려면 **명시적**으로 형변환 연산자를 사용해서 변환해주어야 한다.

```java
class ex {
    public static void maint(String args[]){
    long a = 1_000_000 * 1_000_000;
    long b = 1_000_000 * 1_000_000L;

    System.out.println("a="+a); // a=-7273블라블라 출력. 오버플로우 발생
    System.out.println("b="+b); // b=1000000000000. 의도한 값 출력. 형변환이 잘 이루어졌
}
}
```

#### Math.round()로 반올림하기

- `long result = Math.round(4.52)`,는 result에  5가 저장된다.

#### 문자열의 비교

- 논리 연산자, 비교 연산자를 사용하는건 비슷하나... 문자열의 비교에서는 "=="대신 `equals()`라는 메서드를 사용해야 한다.
  - **"객체"** 가 다르다면 `==`연산자에서 `false`를 반환한다.
  - `equals()`의 경우 객체의 "값"이 동일한지 대해 판단한다.

```java
String str = new String("abc")
boolean result = str.equals("abc") // 문자열의 내용이 같으므로 true 저장됨
```

#### 조건 연산자

- `조건식 ? 식1 : 식2`에서 true이면 식1이, false라면 식2가 실행된다.

- 조건 연산자의 식1, 식2 두개 피연산자의 타입이 다른 경우, 이항 연산자처럼 산술 변환이 발생한다.

```java
x = x + (mod < 0.5 ? 0 : 0.5) // 0과 0.5의 타입이 다르다.
==>x = x + (mod < 0.5 ? 0.0 : 0.5) // 0이 0.0으로 자동 형변환되었다.
```

#### 대입 연산자

- 변수와 같은 저장 공간에 값 또는 수식의 연산결과를 저장하는데 사용된다.

##### lvalue와 rvalue

- 대입 연산자의 왼쪽 피연산자를 `lvalue`, 오른쪽 피연산자를  `rvalue`라고 한다.

- `lvalue`는 반드시 변수처럼 값을 변경할 수 있는 것이어야 한다. `rvalue`는 상관없음.
