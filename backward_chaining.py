goal = ["bird", "eagle"]
facts = [["vertebrate", "eagle"], ["flying", "eagle"],["animal", "eagle"], ["feathers", "eagle"]]
if goal in facts:
    print("The goal", goal[1], "is a", goal[0])
else:
    print("The goal", goal[1], "is not a", goal[0])
