import sys

# taking value of n as input from the commandline
arg=sys.argv
n=int(arg[1])


def fizzbuzz(n):
    #iterating from 1 to n
    for i in range(1,n+1):
	#divisible by 2
	if i%2==0 and i%3!=0:
            print i, " = fizz"
            continue
	#divisible by 3
	if i%3==0 and i%2!=0:
            print i," = buzz"
            continue
	# divisible by both 2 and 3
        if i%2==0 and i%3==0:
            print i," = fizzbuzz"
            continue
        else:
            print i, " is not divisble by 2 or 3"

fizzbuzz(n)
