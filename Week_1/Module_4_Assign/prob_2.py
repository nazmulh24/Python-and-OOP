# --> https://atcoder.jp/contests/arc087/tasks/arc087_a

from collections import Counter


N = int(input())
List = list(map(int, input().split()))

cnt = Counter(List)
remove = 0

for x, freq in cnt.items():
    # print(x, freq)

    if freq > x:
        remove += freq - x
    elif freq < x:
        remove += freq

print(remove)
