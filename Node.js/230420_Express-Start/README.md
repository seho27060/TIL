# Express

## How To Run Server on Express

- `Express` 를 사용하여 `node.js`환경에서 서버를 구축해보자.

- 기타 다른 서버들과 비슷하게, 접근 `url`과 `port`를 지정하여 서버를 구축한다.
  
  - 서버를 올리고, `api`를 등록하고 요청에 따라 값을 반환하는 전반적인 과정이 비슷할 뿐이지,
  
  - `node.js`는 `Observer Pattern`임을 잊지말자.

- `router`와 `server`를 구분하여 파일을 생성하는게 좋다.
  
  - `router`: 경로를 지정(Controller?)
  
  - `server` : 서버 구동

### server.js

- 서버의 구동이 작성되는 파일

- `router`와 `html`의 엔진, 연결 포트(`listen`)등을 설정한다.

```javascript
var express = require('express')
var app = express()

// 경로의 main.js를 불러와 app에 전달
var router = require('./router/main')(app)

// server가 읽을 수 있도록 HTML의 위치 정의
app.set('views', __dirname + '/views')

// HTML 렌더링 시 EJS 엔진을 사용하도록 설정
app.set('views engine', 'ejs')
app.engine('html', require('ejs').renderFile)

var server = app.listen(3000, function() {
  console.log("Express server has started on port 3000")
})

app.use(express.static('public'))
```

### router/main.js

- 서버 경로(router)를 지정하는 파일
- 접근 `url`을 설정하고 접근 시 반환(작동)하는 파일을 매핑한다.

```javascript
// router/main.js
module.exports = function (app){
    app.get('/',function (req,res){
        res.render('index.html')
    })
    app.get('/about', function (req,res){
        res.render('about.html')
    })
}
```

---

- 레퍼런스

> [[Node.JS] 강좌 09편: Express 프레임워크 사용해보기 | VELOPERT.LOG](https://velopert.com/294)
