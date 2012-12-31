def listPrintLineBreaks (origList):
    '''Given a list with one or two layers of additional nested lists, \n
    this function prints the first layer of nested lists with \n
    triple-space line breaks between each item. It double-spaces items \n
    in the second layer, if one exists.'''

    for i in range (len(origList)): ## we want i to be an integer \
##        so that we can refer to origList[i] later on.
        print '\n\n'
        if len (origList[i]) > 1: # i.e. if the list has multiple elements...
##        ...print each element on a separate line.        
            for j in range (len(origList[i])):
                print '\n'
                print origList[i][j]
        else: # i.e. if 
            print origList[i] # This applies to empty lists or \
##            to lists with just one element.
