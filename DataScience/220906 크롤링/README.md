- [크롤링_00](#크롤링_00)
  - [개요](#개요)
    - [웹 크롤러 아키텍쳐](#웹-크롤러-아키텍쳐)
      - [Frontier](#frontier)
      - [Fetcher](#fetcher)
      - [Parser](#parser)
    - [Robots.txt](#robotstxt)

# 크롤링_00

## 개요

- 데이터분석에 있어 많은 프로젝트에서 cold starter(분석 데이터의 부족으로 연구를 시작할 수 없는 문제)를 겪게 된다. 이러한 상황에서 크롤링 기술을 통해 WWW에 흝뿌려진 여러 데이터들을 수집하여, 전처리작업을 거쳐 사용 가능한 데이터로 저장할 수 있다.

- 크롤링은 단순히 특정 url에 접근하여 해당 html을 긁어와 필요 데이터를 css selector를 선택하여 추출해내는 게 아닌, 동적 페이지, SPA, 업데이트로 html구조가 자주 변경되는 페이지, robot.txt를 참고하여 크롤링 윤리를 지키는 기술을 포함한다.

- 파이썬에서의 크롤링 패키지가 애용되나.. 자바에도 있다. 근데 왜 하칠 파이썬을 통한 크롤링이 우세한걸까? 왜 파이썬을 통한 크롤링이여하는가?

### 웹 크롤러 아키텍쳐

#### Frontier

- 탐색할 url을 `Fetcher`에게 전송한다.

#### Fetcher

- 수신받은 url을 통해 페이지에 접근하여 html을 긁어와 `Parser`에게 넘겨준다.

#### Parser

- 수신받은 html을 분석하여 해당 페이지 내의 하이퍼링크(a태그, url)를 찾는다. 

- 찾은 url을 `Fetcher`에게 전달. 순환과정으로 크롤링이 진행된다.

- 위 3개의 아키텍쳐로 크롤링이 진행되며, `Fetcher` - `Parser`간의 순환과정에서 이동할려는 url이 이전에 방문한 중복 url이 아닌가에 대한 기술적 논의도 필요하다.(이미 여러 논문 존재.)

### Robots.txt

> robots.txt 파일은 크롤러가 사이트에서 액세스할 수 있는 URL을 검색엔진 크롤러에 알려 줍니다. 이 파일은 주로 요청으로 인해 사이트가 오버로드되는 것을 방지하기 위해 사용 - Google 검색 센터 Robots.txt 소개

- 사이트의 크롤러 트래픽을 관리

---

- 레퍼런스

> https://velog.io/@mowinckel/%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-I#%F0%9F%A7%AD-fetcher-parser-frontier

> [robots.txt 소개 및 가이드 | Google 검색 센터 &nbsp;|&nbsp; 문서 &nbsp;|&nbsp; Google Developers](https://developers.google.com/search/docs/advanced/robots/intro?hl=ko)
