D, G = map(int,input().split(' '))
pc = [list(map(int,input().split(' '))) for i in range(D)]


ans = 0
for i in range(D):
    ans += pc[i][0]

for i in range(2**D-1):
    temp_ans = 0
    temp_sum = 0
    s = '{:010b}'.format(i)[::-1]
#   print(s)
    notused = -1
    for j in range(D):
        if s[j] == '1':
            temp_ans += pc[j][0]
            temp_sum += (j+1)*pc[j][0]*100 + pc[j][1]
        else:
            notused = j
#    print(notused,temp_ans,temp_sum)
    if temp_sum >= G:
        ans = min(temp_ans,ans)
    else:
        for i in range(1,pc[notused][0]):
            if (notused+1)*i*100+temp_sum >= G:
                ans = min(temp_ans+i,ans)
#                print(ans)
                break
print(ans)