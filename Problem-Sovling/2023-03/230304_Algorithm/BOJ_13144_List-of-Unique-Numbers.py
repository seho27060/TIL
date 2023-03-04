#230304 13144 List of Unique Numbers
# 길이가 n < 100,000인 수열에서
# 길이가 1 이상인 부분 수열을 뽑았을때,
# 중복된 숫자를 가지지 않는 경우의 수를 구하라

n = int(input())
permu = list(map(int,input().split()))

dp = [0]*100001

end = -1
result = 0
answer = 0

for start in range(n):
    while end+1 < n and dp[permu[end+1]] == 0:
        end += 1
        dp[permu[end]] += 1
        result += 1
    answer += result
    result -= 1
    dp[permu[start]] -= 1
print(answer)