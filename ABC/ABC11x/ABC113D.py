
def DP(H, W, K):
    res = [[0 for i in range(W)] for j in range(H+1)]
    res[0][0] += 1
    for step in range(1, H+1):
        for i in range(2**(W-1)):
            s = "{:08b}".format(i)[::-1]
#            print()
#            print(s)
            if '11' in s:
                continue
            for x in range(0, W):
                if x == 0:
                    if s[x] == '0':
                        res[step][x] += res[step-1][x]
                    elif s[x] == '1':
                        res[step][x+1] += res[step-1][x]
                elif x == W-1:
                    if s[x-1] == '0':
                        res[step][x] += res[step-1][x]
                    elif s[x-1] == '1':
                        res[step][x-1] += res[step-1][x]
                else:
                    # right
                    if s[x] == '0' and s[x-1] == '0':
                        res[step][x] += res[step-1][x]
                    elif s[x] == '1':
                        res[step][x+1] += res[step-1][x]
                    elif s[x-1] == '1':
                        res[step][x-1] += res[step-1][x]
#            print(res[step])
        for i in range(W):
            res[step][i] = res[step][i] % MOD
    return res[step][K-1]


H, W, K = map(int, input().split(' '))
MOD = 1000000007
print(DP(H, W, K))
