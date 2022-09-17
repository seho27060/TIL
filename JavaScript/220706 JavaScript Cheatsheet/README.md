- [러닝 리액트(Learning React)](#러닝-리액트learning-react)
  - [Chapter 2. 리액트를 위한 자바스크립트](#chapter-2-리액트를-위한-자바스크립트)
    - [JavaScript CheetSheet](#javascript-cheetsheet)
      - [변수 선언하기](#변수-선언하기)
      - [함수 만들기](#함수-만들기)
      - [객체와 배열](#객체와-배열)
      - [비동기 자바스크립트(asynchronous JavaScript)](#비동기-자바스크립트asynchronous-javascript)
      - [클래스](#클래스)
# 러닝 리액트(Learning React)
## Chapter 2. 리액트를 위한 자바스크립트
### JavaScript CheetSheet

#### 변수 선언하기

1. const 키워드 : 상수(constant)는 값을 변경할 수 없는 변수이다.

    ```javascript
    const pizza = true
    pizza = false //error!!
	```

2. let 키워드 : 변수의 영역을 코드 블록 {} 안으로 한정할 수 있다. == 블록 안에서 글로벌 변수를 보호할 수 있다.

    ```javascript
    var topic = "JS"
    
    if (topic) {
        let topic = "react"
        console.log('block', topic) // block react 출력
    }
    console.log("global", topic) // global JS 출력	
	```

    ```javascript
    for(var i = 0; i < 5; i++){
        div = document.createElement('div')
        div.onclick = funtion(){
            alert(i)
        }
        container.appendChild(div)
    }
    // var i로 인해 i는 global 변수이다. html상의 div 태그는 공통된 i = 5 인 값이 할당된다.
    /////
    for(let i = 0; i < 5; i++){
        div = document.createElement('div')
        div.onclick = funtion(){
            alert(i)
        }
        container.appendChild(div)
    }
    // let i로 인해 i는 block 변수이다. html상의 div 태그에는 i가 각각의 0 ~ 4 에 따라 블록의 값이 저장된다.
    ```

3. 템플릿 문자열

	```javascript
	console.log(lastName + ", " + firstName + " " + middleName)
	console.log('$(lastName), $(firstName) $(middleName)')
	// 위 아래 코드는 같은 값을 출력
	```



#### 함수 만들기

1. 함수 선언 - **호이스팅 가능**

   ```javascript
   function logCompliment() {
       console.log("good job!")
   }
   ```

2. 함수 표현식(function expression) - 호이스팅 불가

   ```javascript
   const logCompliment = function(){
       console.log("good job!")
   }
   
   // 인수 넘기기
   const logCompliment = function(firstName, message){
       console.log('$(firstName): $(message)')
   }
   
   logCompliment("JS","Very Cool") // JS Very Cool 출력
   ```

3. 디폴트 파라미터

   ```javascript
   function logActivity(name ="seho", activity="workingout"){
       console.log('$(name) is $(activity)')
   }
   ////
   
   const defaultPerson = {
       name : {
           first : "hose",
           last : "Park"
       },
       favActivity : "soccer"
   }
   
   function logActivity(p= defalutPerson){
       console.log('$(p.name.first) is $(p.favActivity)')
   }
   ```

   - 함수에 default parameter을 설정할 수 있다.

4. 화살표 함수(Arrow Function) :  function 키워드 없이도 함수 형성 가능/ return 을 사용하지 않아도 식을 계산한 값이 자동으로 반환된다.

   ```javascript
   const lordify = firstName => 'gwangju $(firstName)'
   //// 파라미터가 한개인 경우
   var lordify = (firstName, land) => '$
   (land) $(firstName)'
   //// 파라미터가 두개인 경우
   ```


- 객체 반환하기

    ```javascript
    const person = (firstName, lastName) => ({
        first: firstName,
        last : lastName
    })
    console.log(person("seho", "Park"))
    ```

	- 중괄호 {} 를 할당해야 객체의 값 할당이 가능하다.

- 화살표 함수와 영역

	- 일반 함수는 this를 새로 바인딩(binding)한다. 때문에 화살표 함수를 사용할때 this의 영역이 제대로 유지된다.

  ```javascript
  var gangwon = {
      resorts : {"A","B","C"},
      print : function(delay=1000){
          setTimeout(() => {
            console.log(this.resorts.join(","))
          }, delay)
      }
  }
  ```

  - 화살표 함수를 사용하지 않으면 this는 Window 객체를 갖는다.

#### 객체와 배열

1. 구조 분해(destructuring)를 사용한 대입

   ```javascript
   const sandwich = {
       bread : "crunch",
       meat : "tuna",
       cheese : "american",
       toppings : ['rettuce', 'tomato']
   }
   
   const {bread, meat} = sandwich
   
   console.log(bread, meat) // crunch, tuna 출력
   ```
   
2. 배열 구조 분해하기

   ```javascript
   const [,,thirdAnimal] = ["dog", 'cat', 'turtle']
   
   console.log(thirdAnimal) // turtle
   ```

3. 객체 리터럴 개선(object literal enhancement)

   - 구조 분해의 반대

   ```javascript
   const name = "out"
   const elevation = 1000
   
   const print = function() {
       console.log('$(this.name) is height same as $(this.elevation)')
   }
   const funHike = {name, elevation, print}
   
   funHike.print()
   ```

4. 스프레드 연산자(spread operator)

   - 3개의 점(...) 으로 이뤄진 연산자.

   ```javascript
   const ABC = ["A","B","C"]
   const XY = ["X","Y"]
   const ABCXY = [...ABC, ...XY] 
   
   console.log(ABCXY) // A B C X Y
   ```

   - 레스트 파라미터(rest parameter)

   ```javascript
   function direct(...args) {
       let [start, ...remaining] = args
       let [finish, ...stops] = remaining.reverse()
       console.log('$(start)')
       console.log("$(stops)")
       console.log('$(finish)')
   }
   
   direct("gwangju", 'busan', 'jeju','seoul') // gwangju/ busan jeju/ seoul 순으로 출력.
   ```



#### 비동기 자바스크립트(asynchronous JavaScript)

- 이제까지 예시의 코드는 모두 동기적(synchronous)
- 비동기 작업을 통해 작업 완료를 기다리면서 다음 작업을 수행할 수 있다.

1. 단순한 프라미스와 fetch

   - fetch 함수를 통해 REST API에 요청을 간단하게 보낼 수 있다.

   ```javascript
   fetch("https://urlExample.com").then(res => 	console.log(res.json())
   )
   ```

   - fetch 함수를 통해 요청을 하면 대기중(pending)인 **프라미스(promise)**가 확인된다.
     - 프라미스 : 데이터가 도착하기 전의 상태
   - .then 을 통해 대기중인 프라미스를 연쇄 호출한다.
     - 콜백 함수(callback function)을 인수로 받으며, 바로 앞의 연산(프라미스)가 성공하면 콜백 함수를 호출한다.

   ```javascript
   fetch("https://urlExample.com")
       .then(res => res.json())
   	.then(json => json.results)
   	.then(console.log)
   	.catch(console.error
   ))
   ```

   1. fetch 함수가 url로 GET 요청 전달
   2. 요청 성공시, 응답 데이터가 JSON 으로 변환
   3. JSON 데이터의 results 얻는다
   4. 콘솔에서 출력
   5. 만약 fetch가 성공하지 못한경우 catch의 구문 실행

2. async/ await

   - 비동기 프라미스를 처리하는 async 함수

   ```javascript
   const getFakePerson = async() => {
       try {
           let res = await fetch("https:url.com")
           let {results} = res.json()
           console.log(results)
       } catch(error) {
           console.log(error)
       }
   }
   
   getFakePerson()
   ```

   - getFakePerson 함수에 **async 키워드**가 붙었다. 이는 해당 함수를 **비동기 함수**로 만들어 준다.
   -  **await 키워드**를 붙이면 해당 프라미스가 완료되고 다음 코드가 실행된다.

3. 프라미스 만들기

   - 비동기 요청을 하면 성공하거나/ 오류가 발생하거나 두가지 상황이 나타난다.

   ```javascript
   const getPeople = count =>
   	new Promise((resolves, rejects) => {
           const api = "https://api.randomuser.me/?nat=US&results=$(count)"
           const request = new XHLHttpRequest()
           request.open("GET", api)
           request.onload = () => requust.status === 200 ? resolves(JSON.parse(request.response).results) : rejects(Error(request.statusText))
           request.onerror = err => rejects(err)
           request.send()
       })
   
   getPeople(5)
   	.then(members => console.log(members))
   	.catch(error => console.error('getPeople failed : $(error.message)'))
   ```

   - getPeople 함수는 새로운 프라미스를 반환한다
   - 새로운 프라미스는 API에 요청을 보내고 성공하면 데이터를 읽고, 아니라면 오류를 발생시킨다.
   - getPeople 함수 실행후, then 함수를 연쇄시켜서 반환되는 프라미스가 완료되면 원하는 일을 실행하고, 아니마련 catch를 통해 오류정보를 출력한다.

#### 클래스

- 기존의 Javascript 만의 **프로토타입을 사용한 상속**(
  prototypical inheritance) 라는 방법을 통해 클래스를 생성한다.
- 이젠 class 키워드를 통해 프로토타입 구문에 대한 구문적 편의(syntatic sugar)를 제공한다.

```javascript
class Vacation {
    constructor(destination, length){
        this.destination = detination
        this.length = length
    }
    print() {
        console.log('$(this.destination) has $(this.length) distance')
    }
}

const trip = new Vacation("ameriace", 150)

console.log(trip.print()) // america has 150 distance 출력
```

- constructor 가 생성자 역할을 한다.
- new 를 통해 클래스의 새로운 인스턴스를 생성할 수 있다.

```javascript
class Expedition extends Vacation {
    constructor(destination, length, gear){
        super(destination, length)
        this.gear = gear
    }
    print() {
        super.print()
        console.log('bring your $(this.gear.join("and your"))')
    }
}

const trip2 = new Expedition("japan",3, ["sunglass","flag", "camera"])

trip2.print() 
// japan has 3 distance
// bring your sunglass and your flag and your camera 출력
```

