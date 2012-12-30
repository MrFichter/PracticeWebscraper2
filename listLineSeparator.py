##The purpose of this script is to print
##individual elements of a nested list
##on their own lines.



##Create some lists similar to what my re.findall() function returns in main.py.

testList = [[] , ['a' , 'b' , 'c'] , ['omega']]

##All elements of testList are lists. Some are empty, some have one element,
##and some have multiple elements. We're most ocncerned with those having
##multiple elements.


##main function in this script 
for i in range (len(testList)): # I want i to be an integer so that I can refer to testList[i] later on.
    print '\n\n'
    if len (testList[i]) > 1: # i.e. if the list has multiple elements
        #print each element on a separate line        
        for j in range (len(testList[i])):
            print '\n'
            print testList[i][j]
    else:
        print testList[i] # This applies to empty lists or to lists with just one element.
