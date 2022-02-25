def conditional(a,b):
    # inputs two Boolean variables representing atomic sentences a, b
    # outputs the truth value of the sentence "a -> b"
    return not a or b

def premise1(a,b,c):
    return conditional(not a,not b)

def premise2(a,b,c):
    return a or not c

def premise3(a,b,c):
    return c

def conclusion(a,b,c):
    return b ### ADD CODE HERE

def valid_checker(p1, p2, p3, concl):
    ### ADD CODE IN THIS FUNCTION TO PRINT 'VALID' OR 'INVALID'
    print('a\t b\t c\t p1\t p2\t p3\t conclusion')
    validity =  True
    for a in [True,False]:
        for b in [True,False]:
            for c in [True,False]:
                print(a,'\t',b,'\t',c,'\t',p1(a,b,c),'\t',
                p2(a,b,c),'\t',p3(a,b,c),'\t',concl(a,b,c))
                ### ADD CODE HERE
                if p1(a,b,c) == True and p2(a,b,c)==True and p3(a,b,c)==True and conclusion(a,b,c)==False:
                    validity = False
                    if validity == False: 
                        print("Argument is invalid")
                        return
    print("Argument is valid")
valid_checker(premise1,premise2,premise3,conclusion)