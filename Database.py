def some_we(word):
#    if type(word) !=str:
#        print("come on rnter a bloody word")
#    else:
#         return"well done, {0} is a word".format(word)
    
##OR
    if isinstance(word, str) == True:
        return "well done, {0} is a word". format(word)
    else:
        return 'come on, you\'ve not bloody entered a word'. format(word)                                      