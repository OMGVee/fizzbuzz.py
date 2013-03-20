#!/usr/bin/env python

def fizzThisShit():
        list = range(1,101)
	for i in list:
		a = i%3
		b = i%5
		#print ("a=%s, b=%s" % (str(a), str(b)))
		if (a == 0 and b == 0):
			print ("%d.FizzBuzz" % i)
		elif (a == 0):
			print ("%d.Fizz" % i)
		elif (b == 0):
			print ("%d.Buzz" % i)
		else:
			print ("%d.%d" % (i,i) )


fizzThisShit()
