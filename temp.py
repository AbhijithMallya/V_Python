from collections import defaultdict
jug1,jug2,aim=5,3,4
visited = defaultdict(lambda:False)
def waterjug(amt1,amt2):
    if (amt1==aim and amt2==0)or (amt2==aim and amt1==0):
        print(amt1,amt2)
        return True
    if visited[(amt1,amt2)]==False:
        print(amt1,amt2)
        visited[(amt1,amt2)]=True
        return (waterjug(amt1,0)or
                waterjug(0,amt2)or
                waterjug(jug1,amt2)or
                waterjug(amt1,jug2)or
                waterjug(amt1 + min(amt2 , jug1-amt1) , amt2 - min(amt2 , jug1-amt1))or
                waterjug(amt1 - min(amt1 , jug2-amt2) , amt2 + min(amt1 , jug2-amt2)))
    else : 
        return False
print('Steps')
waterjug(0,0)