[TOC]

# Java_04

## 조건문 제어문

### 여러 조건문

#### if 문

```java
if ( 조건식 ) {
    실행내용
}
```

- 조건식은 `90 <= x && x<= 100`, `str.eauls("yes")`, `str.equalsIngnoreCase("yes)`(대소문자구분없이 문자열비교하는 메서드등등과 같이 사용됨.

#### if-else 문

```java
if ( 조건문 ) {
    실행내용
} else {
    실행내용2
}
```

#### if-else if 문

```java
if (조건식1) {
    실행내용 1
} else if ( 조건식2 ) {
    실행내용 2
} else if ( 조건식3 ) {
    실행내용 3
}
```

#### switch 문

- 조건식을 계산하고, 결과와 일치하는 case문으로 이동한다. 이동후 할당된 내용을 수행하고, break를 만나면 switch 문을 빠져나간다.

```java
switch (조건){
    case 값1 :
        // 실행내용 1
                    
    case 값2 :
        // 실행내용 2
    case 값3 :
        // 실행내
}
```

- 조건식의 결과와 case의 값은 정수 상수. 문자열만 가능하다.



### 여러 반복문

#### for 문

```java
for(int i = 1; i <= 5; i++){
    System.out.println("I can do it");
}
for(초기화; 조건식; 증감식) {
    실행내용
}
```

- "I can do it"을 5번 반복 실행.

#### while 문

```java
while (조건식) {
    실행내용
}
```

#### do-while 문

```java
do {
    실행내용
} while (조건식);
```

- while 문의 변형으로, while문에서 조건식과 블럭{}의 순서를 바꿔놓은 것.

- 블럭 내의 코드의 최소 한번의 실행을 보장한다.

#### break와 continue 문

- break : 만나면 루프 탈출

- continue : 만나면 현재 루프의 실행을 생략하고 다음 반복 루프로 진입.

#### 이름 붙은 반복문

- break은 근접한 단 하나의 반복문만 벗어날 수 있다. 중첩 반복문에서는 곤란할 수 있다.

- 중첩 반복문 앞에 이름을 붙이고 break문과 continue문에 이름을 지정해줌으로, 하나 이상의 반복문을 벗어나거나 반복을 건너뛸 수 있다.

```java
class Ex4_19
{
	public static void main(String[] args)
	{
      // for문에 Loop1이라는 이름을 붙였다..
		Loop1 : for(int i=2;i <=9;i++) {	
				for(int j=1;j <=9;j++) {
					if(j==5)
						break Loop1;
//						break;
//						continue Loop1;
//						continue;
					System.out.println(i+"*"+ j +"="+ i*j);
				} // end of for i
				System.out.println();
		} // end of Loop1

	}
}
```


