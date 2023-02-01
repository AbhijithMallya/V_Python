facts = [["vertibrate","duck"],["flying","duck"],["mammal","cat"]] 
for A1 in facts: 
    if A1[0]=="mammal": 
        facts.append(["vertibrate",A1[1]])
    if A1[0]=="vertibrate": 
        facts.append(["animal",A1[1]])
    if A1[0]=="vertibrate" and ["flying",A1[1]] in facts: 
        facts.append(["bird",A1[1]]) 
print(facts) 

