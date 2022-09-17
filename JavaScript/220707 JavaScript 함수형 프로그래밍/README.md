- [러닝 리액트(Learning React)](#러닝-리액트learning-react)
  - [Chapter 3. 자바스크립트를 활용한 함수형 프로그래밍](#chapter-3-자바스크립트를-활용한-함수형-프로그래밍)
    - [1. 함수형이란?](#1-함수형이란)
    - [2. 명령형 프로그래밍과 선언적 프로그래밍 비교](#2-명령형-프로그래밍과-선언적-프로그래밍-비교)
      - [명령형 프로그래밍(imperative programming)](#명령형-프로그래밍imperative-programming)
      - [선언적 프로그래밍(declarative programming)](#선언적-프로그래밍declarative-programming)
    - [3. 함수형 프로그래밍의 개념](#3-함수형-프로그래밍의-개념)
      - [1. 불변성(immutable)](#1-불변성immutable)
      - [2. 순수 함수(Fure Function)](#2-순수-함수fure-function)
      - [3. 데이터 변환](#3-데이터-변환)
      - [4. 고차 함수](#4-고차-함수)
      - [5. 재귀](#5-재귀)
      - [6. 합성](#6-합성)
# 러닝 리액트(Learning React)

## Chapter 3. 자바스크립트를 활용한 함수형 프로그래밍

### 1. 함수형이란?
- JS에서는 함수가 일등 시민(first class citizen)으로, JS는 함수형 언어이다.
- 함수가 일등 시민 == 함수를 일반적인 데이터와 마찬가지로 취급하겠다.
- JS에서 함수는 저장하고, 읽어오고, 반환하고 등의 기능이 가능하다.

### 2. 명령형 프로그래밍과 선언적 프로그래밍 비교

#### 명령형 프로그래밍(imperative programming)

- 코드로 원하는 결과를 달성해 나가는 과정에만 관심을 두는 프로그래밍 스타일
- 단순한 코드상으로 이해를 위한 주석이 필요함.

```javascript
const string = "Restaurants is indian"
const urlFriendly = ""

for (var i = 0; i < string.length; i++){
    if (string[i] === " "){
        urlFriendly += "-"
    } else {
        urlFriendly += string[i]
    }
}

console.log(urlFriendly) // Restaurants-is-indian 출력
```

#### 선언적 프로그래밍(declarative programming)

- 기능을 이름으로 알 수 있는 함수를 생성하고(추상적인 개념), 과정을 함수로 대체한다.

```javascript
const string = "Restaurants is indian"
const urlFriendly = string.replace(/ /g, "-")

console.log(urlFriendly) // Restaurants-is-indian 출력
```

- 이와 같이 선언적 프로그래밍이 더 읽기 쉽고, 추론하기 쉽다.

### 3. 함수형 프로그래밍의 개념

#### 1. 불변성(immutable)

- 함수형 프로그래밍에서는 데이터는 변할 수 없다.
- 불변성 데이터는 결코 바뀌지 않는다.

```javascript
let list = [
    {title:"red"},
    {title:"grass"},
    {title:"pink"},
]

let addColor = function(title, colors){
    colors.push({title:title})
    return colors
}

// list 가 mutable 하게 데이터가 변경됨
console.log(addColor("Blue", list).length) // 4 출력
console.log(list.length) // 4 출력

let addColor = (title, array) => array.concat({title})
// list 에 대한 객체에 변경함
// list에 대한 변화는 immutable하게 유지된다.
console.log(addColr("blue",list).length) // 4 출력
console.log(list.length) // 3 출력. concat 은 복사된 객체에 대해 처리하고 그 결과를 반환한다.
```



#### 2. 순수 함수(Fure Function)

- 파라미터에 의해서만 반환값이 결정되는 함수.
- 부수 효과(side effect, 전역변수 설정이나 함수내에서 다른 상태(state)를 변경하는것)가 없다.
- == 인수를 변경 불가능한 데이터로 취급함.



- 순수함수 만드는 세가지 규칙

  > 1. 순수 함수는 파라미터를 최소 하나 이상 받아야 한다.
  > 2. 순수 함수는 값이나 다른 함수를 반환해야 한다.
  > 3. 순수 함수는 인자나 함수 밖에 있는 다른 변수를 변경하거나, 입출력을 수행해서는 안된다.



#### 3. 데이터 변환

- 함수형 자바스크립트를 유창하게 사용하기 위해 통달해야 핵심 함수들을 알아보자.

```javascript
const schools = ["newYork", "sydney", "seoul"]

console.log(schools.join(", ")) // "newYork, sydeny, seoul" 출력

const sSchools = schools.filter(school => school[0] === "s")

console.log(sSchools) // ["sydney", "seoul"] 출력
```

```javascript
const highSchools = schools.map(school => '${school} High School')

console.log(highSchools.join("\n"))
// newYork High School
// sydney High School
// seoul High School 출력

const schools2 = {
    "newyork" : 10,
    "washinton" : 2,
    "wakefield" : 5,
}

const schoolArray = Object.keys(schools).map(key => ({
    name: key,
    wins : schools[key],
}))

console.log(schoolArray)
// [ { name:"newyork", wins : 10},
//	 { name:"washinton", wins : 2},
//   { name:"wakefield", wins : 5},]
```

```javascript
const ages = [21,18,42,40,64,63,34]

const maxAge = ages.reduce((max, age) => {
    console.log('${age} > ${max} = ${age > max}')
    if (age > max) {
        return age
    } else {
        return max
    }
}, 0)

console.log('maxAge', maxAge)
// 21 > 0 = true
// 18 > 21 = false
// 42 > 21 = true
// 40 > 42 = false
// 64 > 42 = true
// 63 > 64 = false
// 34 > 64 = false
// maxAge 64 출력
```

- 한 유형의 데이터를 다른 유형으로 변경하는 함수
  1. Array.join("delimiter") : delimiter 로 연결한 문자열 반환/ immutable
  2. Array.filter(output => 조건식) : Array의 인자 output에 대해 조건식이 만족할 경우 해당 output을 포함하는 새로운 배열을 반환
  3. Array.map(변한함수) : 변환함수를 해당 배열의 모든 원소에 적용한 반환값으로 이뤄진 새 배열을 반환한다.
     - Object.keys(Array) : Array의 key 를 반환
  4. Array.reduce(변환함수, 초깃값) : 위를 예시로 max는 초깃값으로 주어진 값을 갖고, age는 배열을 순회하는 값이다. Array의 모든 인자에 대해 변환함수가 실행되고 마지막으로 연속적으로 변환함수가 적용된 1개의 값이 반환된다.(Array.reduceRight  는 reduce와 같은 방식으로 동작하지만 마지막 배열부터 축약(reduce)를 시작한다.)

#### 4. 고차 함수

- 다른 함수를 조작할 수 있는 함수
- 다른 함수를 인자로 받거나 반환하거나, 그 둘을 같이 하기도 한다.
- Array.map, Array.filter, Array.reduce 가 모두 고차 함수이다.

#### 5. 재귀

- 네 재귀 입니다!

#### 6. 합성

- 작은 순수 함수를 연쇄적으로, 병렬적으로 호출하거나 조합하여 더 큰 함수를 만드는 과정을 합성이라고 한다.
- 체이닝(Chaining)이 대표적 기법
