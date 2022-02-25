def conditional(a,b):
    # inputs two Boolean variables representing atomic sentences a, b
    # outputs the truth value of the conditional a->b
    return # fill this in
 
# let’s test it out
print(conditional(True,True))

def combo_sentence(a,b,c,d):
    # inputs four Boolean variables representing atomic sentences a,b,c,d
    # outputs the truth value of the combination (a or b)->(c and d)
    return conditional(a or b,c and d)

def combo_negation(a,b,c,d):
    # inputs four Boolean variables representing atomic sentences a,b,c,d
    # outputs the truth value of the combination not[(a or b)->(c and d)]
    return (a or b) and (not c or not d)

def printTruthTable(sentence1, sentence2):
    # inputs two Boolean variables representing compound sentences, each comprised of 4 atomic sentences
    # outputs a printed truth table for each sentence
    print('a     b     c     d   | sentence1 | sentence2')
    for a in [True,False]:
        for b in [True,False]:
            for c in [True,False]:
			    for d in [True,False]: 
                    print(a, b, c, d, '    ', sentence1(a,b,c,d), '    ', sentence2(a,b,c,d))
               		
# Now let's print a truth table to compare our combo sentence and its negation
print('Truth table for (a or b)->(c and d) and its negation:\n')
printTruthTable(combo_sentence, combo_negation)
