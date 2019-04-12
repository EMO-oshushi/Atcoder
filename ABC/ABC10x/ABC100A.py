N = int(input())
A = list(map(int, input().split(' ')))

A2 = sorted([A[i]-i-1 for i in range(len(A))])
median = A2[len(A)//2]

ans = 0
for i in range(len(A)):
    ans += abs(A2[i]-median)
print(ans)
