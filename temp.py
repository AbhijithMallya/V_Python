# forward chain
facts = [['vertibrates', 'duck'], ['flying', 'duck'], ['mamal', 'cat']]
for A1 in facts : 
    if A1[0]=='mamal':
        facts.append('vertibrates',A1[1])
    if A1[0]=='vertibrates':
        facts.append('animal',A1[1])
    if A1[0]=='mamal':
        facts.append('vertibrates',A1[1])
    
