# 230213 12919 A와 B 2
import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

result = [set() for _ in range(len(b)+1)]
result[len(b)].add(b)

def calculation(cnt):
    if cnt <= len(a):
        return

    for now in result[cnt]:
        if now[-1] == "A":
            result[cnt-1].add(now[:-1])
        if now[0] == "B":
            result[cnt-1].add("".join(reversed(now))[:-1])

    if result[cnt-1]:
        calculation(cnt-1)

calculation(len(b))
#
# for idx in range(1,len(b)+1):
#     print(idx, result[idx])

if a in result[len(a)]:
    print(1)
else:
    print(0)

