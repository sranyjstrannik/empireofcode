from string import ascii_lowercase as a

def golf(p,le=False,u=False,l=False):
        if len(p)==0: return False 
        if len(p)<10 and not le: return False
        le = True
        if not l and p[0] in a: l = True
        elif not u and p[0].upper() in a.upper(): u = True
        else: return False
        if len(p)==1 and u and l and le: return True 
        return golf(p[1:], le,u,l)

assert golf('A1213pokl') == False
assert golf('bAse730onE') == True
assert golf('ULFFunH8ni') == True
