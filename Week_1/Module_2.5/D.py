# --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/O

N = int(input())


# ---------> Fibonacci series code...
def fibo(N):
    f_1, f_2 = 0, 1

    if N == 1:
        return f_1
    elif N == 2:
        return f_2
    else:
        for _ in range(3, N + 1):
            f_1, f_2 = f_2, (f_1 + f_2)

        return f_2


ans = fibo(N)

print(ans)
