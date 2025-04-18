# --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/G


N = int(input())

List = list(map(int, input().split()))

List_C = List[::-1]

if List == List_C:
    print("YES")
else:
    print("NO")
