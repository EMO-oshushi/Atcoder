N = int(input())

ans = [0, 1, 4, 16, 63, ]
for i in range(N+1):
    if i <= 4:
        continue
    ans.append(ans[i-1] * 4 - ans[i-3] - 3 * ans[i-4])
print(ans[N])
