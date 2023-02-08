# 230208-BOJ-선분 교차 2

## 선분 교차 2

- https://www.acmicpc.net/problem/17387

- 복잡한 분기를 하거나.. 공식을 사용한다.

#### 풀이과정

1.  `CCW` 이라는 공식을 사용하면 쉽게 푼다.
   
   - 3개 점 `p1`, `p2`, `p3`가 있을때, `p1`을 기준으로 각 `p2`, `p3`를 잇는 선분이 어떤 방향 관계성을 갖는지 확인 할 수 있다.
   
   - 벡터의 외적을 사용하여 그 값이 음수이면 시계방향, 겹치면 0, 반시계방향일 시 양수의 값을 갖는다.

2. 선분 두개(점 4개)가 주어지니, 각 선분에서 다른 점을 잇는 `CCW`의 값을 계산하여 판단한다.

3. 겹치는 경우(`CCW`가 0인 경우), x값의 범위가 겹치는지, y값의 범위가 겹치는지 확인해줘야 한다.

#### 성과 및 피드백

##### 성과

##### 피드백

#### 레퍼런스

> [[BOJ 17387] 선분 교차 2 - From Math To CS](https://cael0.github.io/problem%20solving/BOJ17387/)
> 
> [[BOJ 17386] 선분 교차 1 - From Math To CS](https://cael0.github.io/problem%20solving/BOJ17386/)
> 
> https://velog.io/@jini_eun/%EB%B0%B1%EC%A4%80-17387%EB%B2%88-%EC%84%A0%EB%B6%84-%EA%B5%90%EC%B0%A8-2-Java-Python
> 
> [CCW(counter clockwise) - gaussian37](https://gaussian37.github.io/math-algorithm-ccw/)
