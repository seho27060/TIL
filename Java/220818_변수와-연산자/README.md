- [Java_01](#java_01)
  - [환경설정](#환경설정)
- [Java_02](#java_02)
  - [변수](#변수)
      - [출력](#출력)
      - [변수의 선언과 저장](#변수의-선언과-저장)
      - [변수의 타입](#변수의-타입)
      - [상수와 리터럴](#상수와-리터럴)
      - [리터럴의 타입과 접미사](#리터럴의-타입과-접미사)
      - [기본형과 참조형](#기본형과-참조형)
      - [printf를 이용한 출력](#printf를-이용한-출력)
    - [화면으로부터 입력받기](#화면으로부터-입력받기)
      - [정수형의 오버플로우](#정수형의-오버플로우)
      - [부호있는 정수의 오버플로우](#부호있는-정수의-오버플로우)
      - [타입 간의 변환방법](#타입-간의-변환방법)
- [Java_03](#java_03)
  - [연산자](#연산자)
      - [형변환 연산자](#형변환-연산자)
      - [자동 형변환](#자동-형변환)
      - [산술 변환](#산술-변환)
      - [Math.round()로 반올림하기](#mathround로-반올림하기)
      - [문자열의 비교](#문자열의-비교)
      - [조건 연산자](#조건-연산자)
      - [대입 연산자](#대입-연산자)
        - [lvalue와 rvalue](#lvalue와-rvalue)

# Java_01

## 환경설정

- 자바 설치하고 eclipse 설치하고 블라블라...

# Java_02

## 변수

#### 출력

```java
class Ex2 {
    public static void main(String args[]){
    System.out.println("Hello, Java") // 출력후 줄바꿈
    System.out.print("3+5=") // 출력후 줄바꿈없음
    System.out.println(3+5) // 3+5=8 로 출력
}
}
```

- `System.out.print/println`

#### 변수의 선언과 저장

- 변수 : 하나의 값을 저장할 수 있는 저장공간

```java
변수타입 변수이름; // 변수 선언 방법
int x; // integer 타입의 변수 x 선언
x = 5; // 변수 x에 5 저장
```

- **Java 코드의 모든 줄에는 세미콜론(;)으로 끝맺는다.**

#### 변수의 타입

| 분류  | 변수의 타입       | 설명                                |
| --- | ------------ | --------------------------------- |
| 숫자  | int, long    | 정수, 20억 넘어가면 long                 |
|     | float,double | 실수, float는 오차없이 7자리/ double은 15자리 |
| 문자  | char         | 문자                                |
|     | String       | 여러 문자                             |

#### 상수와 리터럴

- 상수(constant)는 값이 변경 불가능한 변수/ `final`을 앞에 붙여준다.

```java
final int MAX_SPEED = 10;
```

- 12, 34, "A"와 같은 값들이 원래는 상수, 근데 위와 같이 상수를 java내에서 정의했기 때문에 기존의 상수는 리터럴(literal)이라고 부른다.

#### 리터럴의 타입과 접미사

- float -> f, F/ double -> d,D/ long -> l, L ==> **f와 l은 생략 불가능하다.**

- 'A'와 같은 char은 작은따옴표, "ABD"와 같은 String은 큰 따옴표/ ""에는 아무런 문자가 없는게 허용이지만, ''은 허용되지 않는다.

```java
String name = new String("Java");
String name = "Java" // 위아래 같은 표현이다. 다른 점은 9장에서
```

- 덧셈 연산자에서 숫자와 문자열을 연산시, 문자열로 변환되어 계산된다.

```java
System.out.println(7+7+"") // 14
System.out.println(""+7+7) // 77 출력. 왼 -> 오른 순서로 연산
```

#### 기본형과 참조형

- 기본형 : 논리형(boolean), char, 정수형(byte, short, int, long), 실수형(float, double)

- 참조형 : 객체의 주소를 저장, 기본형을 제외한 나머지 타입.
  
  | 종류\크기 | 1byte   | 2byte | 4byte | 8byte  |
  | ----- | ------- | ----- | ----- | ------ |
  | 논리형   | boolean |       |       |        |
  | 문자형   |         | char  |       |        |
  | 정수형   | byte    | short | int   | long   |
  | 실수형   |         |       | float | double |

#### printf를 이용한 출력

- 지시자(specifier)를 통해 변수의 값을 여러가지 형식으로 변환하여 출력

```java
System.out.printf("age:%d",14) //%d에 14 대입되어 출
```

| 지시자 | 설명                     |
| --- | ---------------------- |
| %d  | 10진수(decimal)          |
| %x  | 16진수(hexa-decimal)     |
| %f  | 부동 소수점(floating-point) |
| %c  | 문자(char)               |
| %s  | 문자열(string)            |

### 화면으로부터 입력받기

```java
import java.util.Scanner // Scanner 클래스 사용을 위한 import
Scanner scanner = new Scanner(System.in) // Scanner 클래스 객체 생성
String input = scanner.nextLine(); // 입력 내용 input에 저장 
int num = Integer.parseInt(input); // input을 int로 변환
==>
int num = scanner.nextInt(); // 위 과정을 하나의 메서드로 가능하다.
```

#### 정수형의 오버플로우

- 지정한 타입이 표현할 수 있는 값의 범위를 넘어가는 경우

- 에러가 발생하는것이 아닌 예상했던 결과를 얻지 못하게 된다.

- 예) 4bit 2진수의 최대값인 "1111"에 1을 더하면 "10000"이 맞지만, java에서는 "0000"으로 계산된다.

#### 부호있는 정수의 오버플로우

- 부호있는 정수(4bit)의 경우 표현범위가 "-8 ~ 7"이므로 해당 범위에서 반복된다.

#### 타입 간의 변환방법

1. 숫자를 문자로 변환 = 3 + '0' -> '3'

2. 문자를 숫자로 변환 = '3' - '0' -> 3

3. 숫자를 문자열로 변환 = 3 + "" -> "3"

4. 문자열을 숫자로 변환 = Integer.parseInt("3") -> 3/ Double.parseDouble("3.14") -> 3.14

5. 문자열을 문자로 변환 = "3".charAt(0) -> '3'

6. 문자를 문자열로 변환 = '3' + "" -> "3"

# Java_03

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

- 컴파일러는 "기존의 값을 최대한 보존할 수 있는 타입으로 자동 형변환한다"

- 보통 표현범위가 좁은 타입 -> 표현범위가 넓은 타입 으로 형변환된다.

#### 산술 변환

- 이항 연산자는 두 피연산자의 타입이 일치해야 연산이 가능하다.

- 피연산자의 타입의 일치를 위해 자동 형변환되는 것을 '산술 변환'이라고 한다.

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
