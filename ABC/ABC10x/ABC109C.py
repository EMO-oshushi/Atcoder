import math
from functools import reduce

N, X = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

A.append(X)
sortedA = sorted(A)
B = [sortedA[i+1] - sortedA[i] for i in range(len(sortedA)-1)]

ans = reduce(math.gcd, B)
print(ans)
