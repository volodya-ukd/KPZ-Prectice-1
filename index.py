def fac(num):
    if num < 1: return "веди норм число"
    if num == 1:
        return num
    else:
        return num * fac(num - 1)


print(fac(5))

