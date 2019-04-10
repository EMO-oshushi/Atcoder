from operator import itemgetter


N, M = map(int, input().split(" "))
AB = [list(map(int, input().split(" "))) for _ in range(N)]
AB = sorted(AB, key=itemgetter(0))

now = 0
ans = 0
for a, b in AB:
    ans += a * min(M-now, b)
    now += min(M-now, b)
    if now == M:
        break
print(ans)
