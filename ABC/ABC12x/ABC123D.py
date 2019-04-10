X, Y, Z, K = map(int, input().split(" "))

A = sorted(map(int, input().split(" ")),reverse=True)
B = sorted(map(int, input().split(" ")),reverse=True)
C = sorted(map(int, input().split(" ")),reverse=True)

AB = []
for a in A:
    for b in B:
        AB.append(a+b)
AB = sorted(AB, reverse=True)
ABC = []
for ab in AB[:K]:
    for c in C:
        abc = ab + c
        ABC.append(abc)
ABC = sorted(ABC, reverse=True)
for ans in ABC[:K]:
    print(ans)
