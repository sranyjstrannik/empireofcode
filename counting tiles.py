# общая длина -- 226
s = """"
from itertools import product as p
def golf(r):
    t = sum([r*r>x for x in [i**2+j**2 for i,j in p(range(4),repeat=2)]])
    q = sum([r*r>=x for x in [i**2+j**2 for i,j in p(range(1,5),repeat=2)]])
    return [q*4,(t-q)*4]
"""

#общая длина -- 148
# решение не зашло, т.к. нельзя использовать numpy
s="""
import numpy as n
def golf(r):
 t=n.arange(4)
 x,y=n.meshgrid(t,t)
 m,k=(x**2+y**2<r**2).sum()*4,((x+1)**2+(y+1)**2<=r**2).sum()*4
 return [k,m-k]
"""

# общая длина 130
s="""
def golf(r):
 p=range(4)
 t=q=0
 for i in p:
  for j in p:
   s=i*i+j*j
   t+=r*r>s
   q+=r*r>=s+2*(i+j+1)
 return [q*4,t*4-q*4]
"""
print(len(s))