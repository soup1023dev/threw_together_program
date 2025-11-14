import random
a = "h"
b = "e"
c = "l"
d = "o"
e = "w"
f = "r"
g = "d"
print("hello_world")
print(a+b+c+c+d,e+d+f+c+g)
print(bytes.fromhex("68656c6c6f20776f726c64").decode("utf-8"))
print(''.join([next(c for c in (chr(random.randint(0,255)) for _ in iter(int,1)) if ord(c)==ord(t)) for t in "hello world"]))
