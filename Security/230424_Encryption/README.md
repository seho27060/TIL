[TOC]

# Security

## Encryption

> **암호화**(暗號化) 또는 **엔크립션**(encryption)은 특별한 지식을 소유한 사람들을 제외하고는 누구든지 읽어볼 수 없도록 [알고리즘](https://ko.wikipedia.org/wiki/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98 "알고리즘")을 이용하여 [정보](https://ko.wikipedia.org/wiki/%EC%A0%95%EB%B3%B4 "정보")([평문](https://ko.wikipedia.org/wiki/%ED%8F%89%EB%AC%B8 "평문")을 가리킴)를 전달하는 과정이다. 이러한 과정을 통해 암호화된 정보([암호문](https://ko.wikipedia.org/wiki/%EC%95%94%ED%98%B8%EB%AC%B8 "암호문"))를 낳는다. 이에 역행하는 과정을 **해독** 또는 **디크립션**(decryption)이라고 하며 이로써 암호화된 정보를 다시 읽을 수 있다. - 위키 백과

- 암호화에서는 "키"를 사용함으로 암호와 그 알고리즘이 노출되어도 해독이 불가능하도록 보안성을 높이게 된다.
  
  - 원문 "P"와 키 값 'K'를 사용하여 "P + K"라는 암호문을 생성하는 방식이라 할 수 있다.

### 암호화의 종류

#### 단방향 암호화

- 신원 증명과 인증과정에서 사용된다. 

- 암호를 원문(평문)으로 해독하는 복호화를 거쳐도 원래의 비밀번호를 알 수 없다.

- 대부분의 경우 **"해시 함수"**(hash function)을 통해 **"해시"** 를 생성하는 해싱과정을 통해 단방향 암호화가 진행된다.

#### 비밀키 암호화

- 말 그대로 비밀키를 사용하여 암호화와 복화화를 거치는 과정을 말한다.
  
  - 양방향 암호화의 일종

- 원문에 이진수 연산 처리하여 암호문을 생성하고
  
  - 암호문을 받은 수신자는 암호화 키 값을 활용한 역산으로 암호문을 해독한다.

- 송신자와 수신자 모두 **동일한 암호화 키**를 소지하여야 한다는 조건이 있다.

#### 공개키 암호화

- 공개키와 개인키를 사용하여 암호화 및 복호화를 진행한다.
  
  - 역시 양방향 암호화의 일종

- 공개키를 통해 암호화를 진행하고
  
  - 개인키를 통해 복호화를 진행한다.

### Node.js에서의 암호화

#### Crypto vs Bcrypt

- `Node.js`에서 기본으로 제공하는 `Crypto`는 여러 해시 함수를 통한 암호화 기능을 제공한다.

- `Bcrypt`는 암호를 해시하는 라이브러리로, `Crypto`에 비해 해싱에 느리고 비용이 많이 다는 `Blowfish`알고리즘으로 구현된다.
  
  - `Crypto`에 비해 강력한 보안이 필요할 때 사용된다.

#### 문제점

- 비밀번호의 예로, 단순히 암호화를 진행했을 경우 **레인보우 테이블**이라는 문제가 발생한다.
  
  - 동일한 비밀번호에 대해 단순한 암호화를 진행했을 경우, 같은 암호값을 같는 경우를 의미한다.

- 위와 같은 상황을 방지하기 위해 `salt`라는 특정 값을 붙여 무작위로 같은 값에 대해 다른 암호값을 같도록 한다.
  
  - 또는 해시 함수를 여러번 적용하기도 한다.

---

- 레퍼런스

> [암호화 - 위키백과, 우리 모두의 백과사전](https://ko.wikipedia.org/wiki/%EC%95%94%ED%98%B8%ED%99%94)
> 
> https://velog.io/@jiheon/Node.js-crypto%EB%A1%9C-%EB%B9%84%EB%B0%80%EB%B2%88%ED%98%B8-%EC%95%94%ED%98%B8%ED%99%94%ED%95%98%EA%B8%B0
> 
> [Node.js - 바람직한 비밀번호 암호화 (crypto) | zinirun](https://zinirun.github.io/2020/12/02/node-crypto-password/)
