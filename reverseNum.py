def is_it_the_same_backwards(x):
	xstr=str(x)
	if xstr[0]=="-":
		return False
	l=len(xstr)
	sp=int(l/2)
	if l%2!=0:
		sp=int((l-1)/2)		
	x1 = xstr[sp:]
	x2 = xstr[:-sp]
	return (list(x1)==list(reversed(x2)))
	
print(is_it_the_same_backwards(121))
