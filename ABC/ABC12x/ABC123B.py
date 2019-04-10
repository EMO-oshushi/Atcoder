needs = [int(input()) for _ in range(5)]

ans = 0
min_wait = 99
for t in needs:
    wait = t % 10
    if wait == 0:
        ans += t
    else:
        min_wait = min(min_wait, t % 10)
        ans += (t // 10 + 1) * 10
if min_wait != 99:
    ans = ans - 10 + min_wait

print(ans)
