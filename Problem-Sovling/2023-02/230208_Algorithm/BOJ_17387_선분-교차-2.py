# 230208 17387 선분 교차 2
# 2개 선분이 교차하는지 구하라
# board의 범위는 -1,000,000 ~ 1,000,000

import sys
input = sys.stdin.readline


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2-x1)*(y3-y2)-(x3-x2)*(y2-y1)

a,b,c,d = map(int,input().split())
e,f,g,h = map(int,input().split())

res1 = ccw(a,b,c,d,e,f)
res2 = ccw(a,b,c,d,g,h)
res3 = ccw(e,f,g,h,a,b)
res4 = ccw(e,f,g,h,c,d)

if res1 == res2 == res3 == res4 == 0:
    if (max(a,c) < min(e,g)) or (max(e,g) < min(a,c)) or (max(b,d) < min(f,h)) or (max(f,h) < min(b,d)):
        print(0)
    else:
        print(1)
elif (res1 * res2 <= 0) and (res3 * res4 <= 0):
    print(1)
else:
    print(0)
