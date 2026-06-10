def convert(num,sys):
    res = ''
    while num:
            res += str(num % sys)
            num //= sys
    return res[::-1] if res else '0'

ans = []
for N in range(1, 100_000):
    R = convert(N, 3)
    T = (N % 3 * 5)
    if N % 3 == 0:
        R = '1' + R + '02'
    else:
        R = R + convert(T, 3)
    R = int(R, 3)
    if R >= 177:
        ans.append([N, R])
print(min(ans))
