# --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/I

T = int(input())

for _ in range(T):

    N = int(input())
    A = list(map(int, input().split()))

    mn = float("inf")

    for i in range(N):
        for j in range(i + 1, N):
            x = A[i] + A[j] + j - i

            mn = min(mn, x)

    print(mn)
