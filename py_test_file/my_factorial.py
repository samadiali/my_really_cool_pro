#returns the factorial of the argument

def my_factorial (n):

	if n <= 0 : #base case
		return 1
	else:
		return n*my_factorial(n-1)
n=0
for i in range (1,n):
		n = n * i  

ab = my_factorial (0)
print ab

