# --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/N

A, B = map(int, input().split())

S = input()

flag = True

for i in range(len(S)):
    if (i == A and S[i] != "-") or (i != A and S[i] == "-"):
        flag = False

if flag:
    print("Yes")
else:
    print("No")
