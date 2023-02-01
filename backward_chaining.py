goal = ["bird", "eagle"]
facts = [["vertebrate", "eagle"], ["flying", "eagle"],["animal", "eagle"], ["feathers", "eagle"]]

def query_fact(fact):
    global facts
    if fact in facts:
        return True
    else:
        return False

def backward_chain(goal):
    if query_fact(goal):
        return True
    else:
        for fact in facts:
            if fact[0] == goal[0]:
                if backward_chain([fact[1], goal[1]]):
                    return True
    return False
    
result = backward_chain(goal)
if result:
    print("The goal", goal[1], "is a", goal[0])
else:
    print("The goal", goal[1], "is not a", goal[0])
