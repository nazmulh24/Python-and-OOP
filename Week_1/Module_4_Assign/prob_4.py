# --> https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/P


N = int(input())
List = list(map(int, input().split()))

op = 0
flag = True

while flag:
    for i in range(len(List)):
        # print(List[i])

        if List[i] % 2 == 1:
            flag = False
            break
        else:
            List[i] //= 2

    if flag:
        op += 1

print(op)

################

# op = 0

# while all(x % 2 == 0 for x in List):
#     List = [x // 2 for x in List]
#     op += 1

# print(op)
