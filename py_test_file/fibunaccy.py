


""" fibonachi (2)
	number --> number

	>>> fibonachi (3)
	2

	fibonachi : [0,1,1,2,3,5,8]
				[0-1-2-3-4-5-6]

	n= 5

	list_fibonachi = [0,1]

	list_fibonachi.append ( list_fibonachi[2nd] + list_fibonachi [1st])
	while i < n:
		list_fibonachi.append ( list_fibonachi[i+1] + list_fibonachi [i])
		i = i + 1
	print list_fibonachi [n] """

def fibonachi (n):
	i= 0
	list_fibonachi = [0,1]

	#list_fibonachi.append ( list_fibonachi[2nd] + list_fibonachi [1st])
	while i < n:
		list_fibonachi.append ( list_fibonachi[i+1] + list_fibonachi [i])
		i = i + 1
	print list_fibonachi [n]





def fibonachir (n):
	print 
	if n== 0:
		return 0
	elif n== 1:
		return 1
	else:
		return (fibonachir(n-1) + fibonachir(n-2))



r = 19
fibonachi (r)
print (fibonachir (r))