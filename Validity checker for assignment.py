#using code from session 3.1
def conditional(a, b):
    #inputs two variables 
    #gives boolean output for a --> b
    return not a or b

#defining the first premise
def premise1(p, q, r, s, t, u, v):
    #gives boolean output for p --> q
    return conditional(not p, not q)
#defining the second premise
def premise2(p, q, r, s, t, u, v):
    #gives boolean output for q --> r
    return conditional( not q, not r)
#defining the third premise
def premise3(p, q, r, s, t, u, v):
    #gives boolean output for s v t
    return s or t
#defining the fourth premise
def premise4(p, q, r, s, t, u, v):
    #gives boolean output for ~t
    return not t
#defining the fifth premise
def premise5(p, q, r, s, t, u, v):
    #gives boolean output for s
    return s
#defining the sixth premise
def premise6(p, q, r, s, t, u, v):
    #gives boolean output for r --> s
    return conditional(not r, not s)
#defining the seventh premise
def premise7(p, q, r, s, t, u, v):
    #gives boolean output for u --> v
    return conditional(not u, not v)
#defining the eight premise
def premise8(p, q, r, s, t, u, v):
    #gives boolean output for ~v
    return not v
#defining the conclusion
def conclusion(p, q, r, s, t, u, v):
    #gives boolean output for p & ~u
    return p and not u
#defining the function that checks validity
def valid_checker(P1, P2, P3, P4, P5, P6, P7, P8, concl):
    print('p\t, q\t, r\t, s\t, t\t,u\t, v\t, P1\t, P2\t, P3\t, P4\t, P5\t, P6\t, P7\t, P8\t, conclusion')
    validity = True # set variable value
    #setting up iteration
    for p in [True, False]:
        for q in [True, False]: 
            for r in [True, False]:
                for s in [True, False]:
                    for t in [True, False]:
                        for u in [True, False]:
                            for v in [True, False]:
                                #printing truth table
                                print(p,'\t',q,'\t',r,'\t',s,'\t',t,'\t',u,'\t',v,'\t',
                                P1(p, q, r, s, t, u, v),'\t',P2(p, q, r, s, t, u, v),'\t',P3(p, q, r, s, t, u, v),'\t',
                                P4(p, q, r, s, t, u, v),'\t',P5(p, q, r, s, t, u, v),'\t',P6(p, q, r, s, t, u, v),'\t',
                                P7(p, q, r, s, t, u, v),'\t',P8(p, q, r, s, t, u, v),'\t',concl(p, q, r, s, t, u, v))
                                #checking the validity
                                if P1(p, q, r, s, t, u, v) == True and P2(p, q, r, s, t, u, v) == True and P3(p, q, r, s, t, u, v) == True and P4(p, q, r, s, t, u, v) == True and P5(p, q, r, s, t, u, v) == True and P6(p, q, r, s, t, u, v) == True and P7(p, q, r, s, t, u, v) == True and P8(p, q, r, s, t, u, v) == True and conclusion(p, q, r, s, t, u, v) == False:
                                    validity == False #changing the variable value
                                    if validity == False:
                                        print("Argument is invalid")
                                        return
    print("Argument is valid")    
#calling the function
valid_checker(premise1, premise2, premise3, premise4, premise5, premise6, premise7, premise8, conclusion)