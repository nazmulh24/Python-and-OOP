# --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/Y

N, Q = map(int, input().split())

List = list(map(int, input().split()))

p_sum = [0] * (N + 1)
for i in range(1, N + 1):
    p_sum[i] = p_sum[i - 1] + List[i - 1]

while Q > 0:
    Q -= 1

    L, R = map(int, input().split())

    ans = p_sum[R] - p_sum[L - 1]

    print(ans)
