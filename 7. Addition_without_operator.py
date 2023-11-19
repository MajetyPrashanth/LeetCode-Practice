a,b = 1,6
num = 0xffffffff
while b != 0:
    tmp = (a & b) << 1
    a = (a ^ b) & num
    b = tmp & num
    if a > num // 2:
        print(~(a ^ num))
    else:
        print(a)
