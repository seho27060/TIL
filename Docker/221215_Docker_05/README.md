[TOC]

# Docker & Kubernetes 05

## Docker로 다중 컨테이너 애플리케이션 구축하기

- 데이터베이스, 백엔드, 프론트엔드 3개의 블록을 각각 컨테이너로 실행하고 네트워크를 활용해 상호간 통신을 구축해보자

- 호스트 머신으로 연결
1. 데이터베이스 컨테이너 실행

2. 백엔드 컨테이너 실행

3. 프론트엔드 컨테이너 실행
- 네트워크를 활용하여 연결
  
  - React의 경우 JavaScript가 브라우저에서 실행되므로 도커의 url 식별자를 사용할 수 없다.

---

- 레퍼런스

> [Udemy - Docker & Kubernetes : 실전 가이드](https://www.udemy.com/course/docker-kubernetes-2022/)
