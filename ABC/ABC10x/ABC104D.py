def calc_ABC(a, c, bq, aq):
    ans = 0
    if aq != 0:
        if bq != 0:
            ans = ans + (a*pow(3, bq, MOD) + bq*pow(3, bq-1, MOD)) \
                 * (c*pow(3, aq, MOD) + aq*pow(3, (aq-1), MOD))
        else:
            ans = ans + (a*pow(3, bq, MOD)) \
                 * (c*pow(3, aq, MOD) + aq*pow(3, (aq-1), MOD))
    else:
        if bq != 0:
            ans = ans + (a*pow(3, bq, MOD) + bq*pow(3, bq-1, MOD)) \
                 * (c*pow(3, aq, MOD))
        else:
            ans = ans + (a*pow(3, bq, MOD)) \
                 * (c*pow(3, aq, MOD))
    return ans % MOD


MOD = 10**9 + 7
S = input()
ans = 0
count_a = 0
count_c = S.count('C')
count_afterq = S.count('?')
count_beforeq = 0

for i in range(len(S)):
    if S[i] == 'A':
        count_a += 1
    elif S[i] == 'B':
        ans += calc_ABC(count_a, count_c, count_beforeq, count_afterq)
        ans = ans % MOD
    elif S[i] == 'C':
        count_c -= 1
    elif S[i] == '?':
        count_afterq -= 1
        ans += calc_ABC(count_a, count_c, count_beforeq, count_afterq)
        ans = ans % MOD
        count_beforeq += 1
print(ans)
