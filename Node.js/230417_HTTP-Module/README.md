# HTTP Module

## HTTP 로 Server-Client 통신하기

- 간단한 구현을 통해 서버를 올리고, 클라이언트가 서버에 요청을 보내는 것을 구현해보자.

- `Server.js` - 서버 역할을 한다.
  
  ```javascript
  var http = require('http')
  var fs = require('fs')
  var url = require('url')
  
  // 서버 생성
  http.createServer(function(request, response){
    var pathname = url.parse(request.url).pathname
  
    console.log("Request for " + pathname + " rece        ived.")
    // url에 다른 요청이 없을 시, 초기화하여 `index.html`을 출력한다.
    if(pathname == "/"){
      pathname = "/index.html"
    }
  
    // 요청 url(pathname)이 없으면 404를 반환하고
    // 아니라면 200과 응답값을 출력한
    fs.readFile(pathname.substr(1), function (err, data){
      if (err) {
        console.log(err)
  
        response.writeHead(404, {'Content-Type': 'text/html'})
      } else {
        response.writeHead(200, {'Content-Type': 'text/html'})
  
        response.write(data.toString())
      }
  
      response.end()
    })
  }).listen(8081)
  
  console.log('Server running at http://127.0.0.1:8081/')
  ```

- `client.js` - 클라이언트 역할을 한다.
  
  ```javascript
  var http = require('http')
  // 요청을 위한 옵
  var options = {
    host: 'localhost',
    port: '8081',
    path: '/index.html'
  }
  
  var callback = function(response){
    var body = ''
    // Event Loop에서와 같이 `.on`을 통해 이벤트를 지정한다.
    // 'data' 이벤트 발생시, 할당된 함수를 실행한다.
    response.on('data', function(data) {
      body += data
    })
  
    // 역시 `.on`을 통해 'end`라는 이벤트를 할당한다.
    // 'end' 이벤트 발생시 body를 출력하고 요청을 끝낸다
    response.on('end',function(){
      console.log(body)
    })
  }
  
  var req = http.request(options,callback)
  req.end()
  ```

---

- 레퍼런스

> [[Node.JS] 강좌 06편: Callback Function 개념 | VELOPERT.LOG](https://velopert.com/255)
> 
> [[Node.JS] 강좌 07편: Event Loop | VELOPERT.LOG](https://velopert.com/267)
