import random
import matplotlib.pyplot as plt
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
plt.figure(figsize=(8,3))
plt.plot([0,0,0,0.5,0.5,0.5], [0,1,0.5,0.5,1,0], 'b', linewidth=3)
plt.plot([1,1,1.5,1,1,1.5,1,1,1.5], [0,1,1,1,0.5,0.5,0.5,0,0], 'b', linewidth=3)
plt.plot([2,2,2.5], [1,0,0], 'b', linewidth=3)
plt.plot([3,3,3.5], [1,0,0], 'b', linewidth=3)
plt.plot([4,4.5,4.5,4,4,4],[1,1,0,0,0,1], 'b', linewidth=3)
plt.axis('equal')
plt.axis('on')
plt.show()
