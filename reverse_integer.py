#function of reversing a number

def reverse(x):
	n=x
	r=0
	while x!=0:
		r = x%10 + r*10
		x = x//10
	print("Number before reversing",n)
	print("Number after reversing",r)


#taking input from user

x=int(input("Enter the number to be reversed.... "))
reverse(x)    #calling a function reverse
