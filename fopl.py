def resolution(c11,c12):
    c1=c11.copy()
    c2=c12.copy()
    c1 = [ -literal for literal in c1]
    for literal in c1:
        if literal in c2 : 
            c1.remove(literal)
            c2.remove(literal)
        elif -literal in c2 : 
            c1.remove(literal)
            c2.remove(-literal)
    if c1 != c11 or c2!=c12 :
        return c1+c2
    else:
        return None
c11 = [1,2,3,5]
c12 = [1,3,4,6]
result = resolution(c11,c12)
print(result)
#OUTPUT --> [-2, -5, 4, 6]