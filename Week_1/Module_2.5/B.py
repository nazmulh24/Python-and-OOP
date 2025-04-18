# --> https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/M

A, B = map(int, input().split())


def is_lucky(num):
    for digit in str(num):
        if digit not in "47":
            return False
    return True


lucky_num = []
for i in range(A, B + 1):
    if is_lucky(i):
        lucky_num.append(i)


if lucky_num:
    for i in lucky_num:
        print(i, end=" ")
else:
    print("-1")
