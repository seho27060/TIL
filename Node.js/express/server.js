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