N = int(input())
if N == 0:
    print('0')
    exit()
check = 1
now = 0
ans = ''
count = 1
while True:
    check *= 2
    a = N%check
#    print(a,count,now)
    if now == N:
        break    
    else:
        if (a-now)%check != 0:
            ans = ans + '1'
            now += count
        else:
            ans = ans + '0'
        count *= -2

print(ans[::-1])
