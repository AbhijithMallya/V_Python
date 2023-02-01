def human(curtokens) :
    take = int(input('Enter how many tokens you want [1-3] : '))
    if( take<1 or take>3):
        print('take only 1-3 tokens')
        human(curtokens)
    global tokens
    tokens = curtokens-take
    print('Human takes {} tokens\nRemaining tokens ={}'.format(take,tokens))
    if(tokens==0):
        print('Human wins')
    

def computer(curtokens):
    take = curtokens%4
    global tokens
    tokens = curtokens-take
    print('Computer takes {} tokens\nRemaining tokens ={}'.format(take,tokens))
    if(tokens==0):
        print('Computer wins')
        
tokens = 12
while(tokens>0):
    human(tokens)
    computer(tokens)