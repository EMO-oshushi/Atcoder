MOD = 10**9+7
N = int(input())

memo = [{} for i in range(N+1)]


def ok(last4):
    bad = ["AGC", "ACG", "GAC", "AGGC", "ATGC", "AGTC"]
    for b in bad:
        if b in last4:
            return False
    return True


def dfs(cur, last3):
    if last3 in memo[cur]:
        return memo[cur][last3]
    if cur == N:
        return 1
    ret = 0
    for c in "AGCT":
        if ok(last3+c):
            ret += dfs(cur+1, last3[1:]+c)
    memo[cur][last3] = ret
    return ret % MOD

print(dfs(0, "TTT"))
