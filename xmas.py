from random import randint
from time import sleep
from os import system
rnd_1 = randint(1,30)

def xmas_tree():
	system("cls")
	for x in range(1,30,2):
		rnd_2 = randint(1,rnd_1)
		if x == 1:
			ch = "$"
		elif rnd_2%4 == 0:
			ch = "o"
		elif rnd_2%3 == 0:
			ch = "i"
		else:
			ch = "*"
		print("{:^33}".format(ch*x))
	print("{:^33}".format("|||"))
	print("{:^33}".format("|||"))
	sleep(.75)
	xmas_tree()

xmas_tree()