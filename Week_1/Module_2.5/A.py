# --> https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/I

N = input()

N_R = N[::-1]

print(int(N_R))

if N == N[::-1]:
    print("YES")
else:
    print("NO")
