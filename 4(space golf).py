# самый короткий из всех мной написанных вариант
import itertools as i,functools as f
#golf_=lambda l:round(min(f.reduce(lambda a,x:a+((x[0][0]-x[1][0])**2+(x[0][1]-x[1][1])**2)**0.5,
#                                 zip(((0,0),)+l,l),0) for l in i.permutations(l)),2)
#длина 185

import itertools as i,functools as f,math as m
golf=lambda l:round(min(f.reduce(lambda a,x:a+m.hypot(x[0][0]-x[1][0],x[0][1]-x[1][1]),
                                 zip(((0,0),)+l,l),0) for l in i.permutations(l)),2)
#длина 187

print(golf({(2, 2), (2, 8), (8, 8), (8, 2), (5, 5)}))