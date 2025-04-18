# --> https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/Q


S = input()

# R = " ".join(word[::-1] for word in S.split())
R = " ".join(map(lambda word: word[::-1], S.split()))

print(R)
