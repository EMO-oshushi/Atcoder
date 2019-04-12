def Base_10_to_n(X, n):
    if (int(X/n)):
        return Base_10_to_n(int(X/n), n) + str(X % n)
    return str(X % n)


N, A, B, C = map(int, input().split(" "))
bamboos = [int(input()) for _ in range(N)]
ans = float("inf")
for i in range(4**N):
    now = Base_10_to_n(i, 4).zfill(N)
    length = [0, 0, 0, 0]
    cost = 0
    for j, c in enumerate(now):
        for k, num in enumerate("0123"):
            if c == num:
                length[k] += bamboos[j]
                break
    if length[0]*length[1]*length[2] == 0:
        continue
    cost += 10 * (now.count('0')-1)
    cost += 10 * (now.count('1')-1)
    cost += 10 * (now.count('2')-1)
    cost += abs(A-length[0])
    cost += abs(B-length[1])
    cost += abs(C-length[2])
    ans = min(cost, ans)
print(ans)
