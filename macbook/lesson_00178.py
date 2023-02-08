# напишите код, который переводит целое число в строку,при том
# что его можно применить в любой системе счисления

def f(n):
    s = str(n)
    return s
res = f(int('ABC', 16))
print(res, type(res))
r = int('ABC', 16)
print(r, type(r))
