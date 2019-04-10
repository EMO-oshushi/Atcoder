import heapq

X, Y, Z, K = map(int, input().split(" "))

A = sorted(map(int, input().split(" ")), reverse=True)
B = sorted(map(int, input().split(" ")), reverse=True)
C = sorted(map(int, input().split(" ")), reverse=True)

anslist = []
flag = {}

heapq.heappush(anslist, (-(A[0]+B[0]+C[0]), (0, 0, 0)))


for _ in range(K):
    p = heapq.heappop(anslist)
    while p[1] in flag:
        p = heapq.heappop(anslist)
    print(p[0]*(-1))
    a, b, c = p[1]
    flag[a, b, c] = True
    # push
    for i, j, k in [[1, 0, 0], [0, 1, 0], [0, 0, 1]]:
        if a+i >= X or b+j >= Y or c+k >= Z:
            continue
        tmp = (a+i, b+j, c+k)
        heapq.heappush(anslist, (-(A[a+i]+B[b+j]+C[c+k]), tmp))
