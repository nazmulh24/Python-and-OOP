# --> https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s


S = input()

temp = ""
ans = []

cur_bal = 0
bal_cnt = 0

for ch in S:

    temp += ch

    if ch == "L":
        cur_bal += 1
    elif ch == "R":
        cur_bal -= 1

    if cur_bal == 0:

        bal_cnt += 1

        ans.append(temp)
        temp = ""

print(bal_cnt)

for A in ans:
    print(A)
