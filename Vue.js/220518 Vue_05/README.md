- [Vue\_05](#vue_05)
	- [Vue Front](#vue-front)
	- [Vue Router](#vue-router)
		- [404 page](#404-page)
			- [404 Component](#404-component)
		- [Navigation Guard](#navigation-guard)
			- [전역 가드(Global Before Guards)](#전역-가드global-before-guards)
		- [Vuex Module](#vuex-module)
			- [Module 분리](#module-분리)
			- [Vue front에서의 출력과정.](#vue-front에서의-출력과정)
	- [Vuex - Component 구성](#vuex---component-구성)
		- [Accounts Login](#accounts-login)
		- [Article Read/ Like](#article-read-like)
			- [Read](#read)
			- [Like](#like)
		- [Artcle CUD](#artcle-cud)
			- [Create](#create)
		- [Comment CRUD](#comment-crud)
			- [Create](#create-1)
			- [Read](#read-1)
			- [Update](#update)
			- [Delete](#delete)


# Vue_05
## Vue Front
- Vue(front)에서 Server에 데이터(json)요청. 여기서 Server는 Django로 구축되어 있다. Django는 DRF를 이용하여 데이터를 serializing 하고 json 파일로 데이터를 넘겨준다.


## Vue Router
### 404 page
#### 404 Component
- views에 HTTP 404가 발생했을때, 출력가능한 Vue instance를 추가한다. 
- router에는 프로젝트 내에서 정의하지 않은 url이나 잘못된 경로일 경우 모두(\*)를 지칭하여 views 404 component로 redirection 하도록 한다.
	###### 404 Not Found 시나리오
	1. Vue Router에 등록되지 않은 routes일 경우
	2. Vue Router에는 등록되어 있지만, 서버에서 해당 리소스를 찾을 수 없는 경우
		ex) /articles/<존재하지않는번호>
		
### Navigation Guard
#### 전역 가드(Global Before Guards)
```js
// @/router/index.js

const routes - [. . .]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

router.beforeEach((to, from, next) =>{
	...
})
expirt default router
```
1. 목표로 하는 URLL로 이동할때마다, 이동하기 전 모든 경우에 발생.
2. router 객체의 메서드
	- to : 이동하려는 route정보/ from : 출발 route의 정보/ next : 실제 route의 이동을 조작하는 함수
3. 해당 메서드의 마지막은 반드시 next()를 실행줘야 이동이 됨.
- URL로 이동 전 인증검사, 필요사항 검사 등의 작업을 실행하고 원래 목적 URL로 이동하던지, 추가 작업을 유도하도록 하는 URl이동하던지 결정하여 작업할 수 있다.

### Vuex Module
#### Module 분리
1. Vuex의 store/index.js 의 1개의 단일 파일에 모든 app의 기능을 담아 작성한다면, 프로젝트에서 다양한 기능의 app이 추가될때마다 단일파일의 코드량이 많아지므로 유지보수에 문제가 생긴다.
2. 이에 따라 app별 기능에 따라 state, getters, mutations, actions를 모듈(파일)로 분리한다.

- store/modules/ 에 appname.js 파일을 만들고, 해당 app별 파일에 기능을 작성을한다.
- store/index.js 의 단일 파일에서 modules의 app별 파일을 import하여 등록한다.


#### Vue front에서의 출력과정.
1. 데이터입력 or url 이동
2. 변경된 데이터가 있다면 해당 기능의 actions 실행
3. (필요하다면 mutations 실행) 이후 getters를 통해 데이터 자동 갱신
4. 출력창에서 getters를 import 하여 출력한다.

## Vuex - Component 구성
- 무조건 store - state에 데이터를 저장하는게 아닌, 컴포넌트 내부, 컴포넌트 간, 등 관계와 상황에 따라 컴포넌트 내에서 state를 설정하여 사용하던지, store에서 데이터를 import하던지 결정하도록 한다.(무조건 중앙통제로 데이터 저장하는건 옳지않다.)

### Accounts Login

- 비동기 통신(axios)로 백엔드 서버와 통신
- saveToken, 사용 유저 변경.

### Article Read/ Like
#### Read

#### Like


### Artcle CUD
#### Create
- vuex 에서 관련 action 선언
	- axios로 url, method 설정
	-  vue에서 input 데이터를 받고 actions의 axios에 사용한다.



### Comment CRUD
#### Create
#### Read

- 굳이 store에 저장하지 않고 두 개의 Vue instance 관계간 데이터 교환(props, emit)을 사용하여도 된다.(상황에 따라 적절히)

#### Update
#### Delete
