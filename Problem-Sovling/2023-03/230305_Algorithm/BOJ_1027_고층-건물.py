# 230305 1027 고층 건물
#  A B를 잇는 직선 공식구하고
# 그 사이 값들이 직선 아래에 있는지 확인

n = int(input())
buildings = [0]
buildings.extend(list(map(int,input().split())))

def findStraightLine(A,B):
    incli = ((B[1]-A[1])/(B[0]-A[0]))
    inter = A[1] - A[0]*incli

    return incli, inter

answer = -1
for now in range(1,n+1):
    result = 0
    for nxt in range(1,n+1):
        check = True

        if now != nxt:
            incli, inter = findStraightLine([now,buildings[now]],[nxt,buildings[nxt]])
            for mid in range(min(now,nxt)+1,max(now,nxt)):
                if buildings[mid] >= incli*mid+inter:
                    check = False
                    break
        if check and now != nxt:
            result += 1
    answer = max(answer,result)
print(answer)