def gcd(a,b):
    a,b = map(int,sorted([a,b],reverse=True))
    while b:
        a, b = b, a%b
    return a

class roll:
    def __init__(self,a,b=None):
        self.a=a
        self.b=b if b else 1
        t = gcd(self.a,self.b)
        self.a=int(self.a/t)
        self.b=int(self.b/t)
        
    def __add__(self,other):
        b1 = self.b
        b2 = other.b
        return roll(self.a*b2+other.a*b1,b1*b2)

def divide_pie(groups):
    s = sum(map(abs,groups))
    res = roll(1)
    for g in groups:
        if g>0: res=res+roll(-g,s)
        else: res=res+roll(res.a*g,res.b*s)

    return (res.a,res.b if res.a else 1)

if __name__ == '__main__':
    assert tuple(divide_pie((15, 33, 37, 16, -1, 22, -73, 66, -59, 10, -39, 57)))==(2682139399739,14362129722368)
    # These "asserts" using only for self-checking and not necessary for auto-testing
    #assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    #assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    #assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    #assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    #assert tuple(divide_pie((10,))) == (0, 1), "All together"
    print("Code's finished? Earn rewards by clicking 'Check' to review your tests!")
