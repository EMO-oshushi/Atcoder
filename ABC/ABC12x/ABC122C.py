N, Q = map(int, input().split(" "))
S = input()
LR = [input() for _ in range(Q)]

rightmax = [0 for i in range(N+1)]
before = S[0]
nowAC = 0
for i, c in enumerate(S):
    if before == "A" and c == "C":
        nowAC += 1
    before = c
    rightmax[i+1] = nowAC
for query in LR:
    l, r = map(int, query.split(" "))
    print(rightmax[r] - rightmax[l])
