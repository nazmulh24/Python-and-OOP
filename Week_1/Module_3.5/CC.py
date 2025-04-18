# --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/M


N = int(input())

List = []

List = list(map(int, input().split()))

mx, mn = max(List), min(List)

for i in range(len(List)):
    if List[i] == mx:
        List[i] = mn
    elif List[i] == mn:
        List[i] = mx

for i in range(len(List)):
    print(List[i], end=" ")
