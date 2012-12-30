>>> lst = ['dog' , 'cat' , 'monkey']
>>> len (lst)
3
>>> for i in range (0, 3): print i, '1'

0 1
1 1
2 1
>>> newList = [lst[0], '\n', lst[1], lst[2]]
>>> print newList
['dog', '\n', 'cat', 'monkey']
>>> for i in range (0, len(lst)):
	newList = [lst[i], '\n']

	
>>> print newList
['monkey', '\n']
>>> ### Why didn't it return 'dog' , '\n' , 'cat' , '\n' , 'monkey' ?
>>> # If I could get it to, I could get more printable results to use around line 48.
