#!/usr/bin/python3
import random
a=0
def myroll():
         return random.randint(1,6)	
while(a<=100):
		n=input("press r ro roll the dice")
		if(n=='r'):
			r=myroll()
			a=a+r
			print("new position is",a)
    