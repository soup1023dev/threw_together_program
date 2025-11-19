# python hello Tutorial.
# ゆっくり内容を理解してみてね！
import random
import matplotlib.pyplot as plt
import pandas as pd
import torch,torch.nn as nn
from flask import Flask
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
plt.figure(figsize=(8,3)); plt.plot([0,0,0,0.5,0.5,0.5], [0,1,0.5,0.5,1,0], 'b', linewidth=3); plt.plot([1,1,1.5,1,1,1.5,1,1,1.5], [0,1,1,1,0.5,0.5,0.5,0,0], 'b', linewidth=3); plt.plot([2,2,2.5], [1,0,0], 'b', linewidth=3); plt.plot([3,3,3.5], [1,0,0], 'b', linewidth=3); plt.plot([4,4.5,4.5,4,4,4],[1,1,0,0,0,1], 'b', linewidth=3); plt.axis('equal'); plt.axis('on'); plt.show()
print(pd.DataFrame({'hello': ['hello', 'hello', 'hello'], 'world': ['world', 'world', 'world']}))

# AIzone====

t="Hello World "*2;C=sorted(set(t));s={c:i for i,c in enumerate(C)};S={i:c for i,c in enumerate(C)}
d=torch.tensor([s[c] for c in t]);x,y=d[:-1],d[1:]
class M(nn.Module):
 def __init__(s,v,h=128):super().__init__();s.e=nn.Embedding(v,h);s.l=nn.LSTM(h,h,batch_first=True);s.f=nn.Linear(h,v)
 def forward(s,x,h=None):o,h=s.l(s.e(x),h);return s.f(o),h
m=M(len(C));o=torch.optim.Adam(m.parameters(),lr=.003);L=nn.CrossEntropyLoss()
for _ in range(2000):p,_=m(x.unsqueeze(0));l=L(p.squeeze(0),y);o.zero_grad();l.backward();o.step()
i=s["H"];h=None;u="H"
for _ in range(11):p,h=m(torch.tensor([[i]]),h);i=torch.argmax(p[0,0]).item();u+=S[i]
print(u)

# end=======
#last
app=Flask(__name__); app.route("/")(lambda: "Hello World"); app.run(debug=True)
