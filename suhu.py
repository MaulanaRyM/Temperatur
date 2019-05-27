#!/usr/bin/python
#Author Mr.yM
import os
from time import sleep

blue = '\033[34;1m'
green = '\033[32;1m'
purple = '\033[35;1m'
cyan = '\033[36;1m'
red = '\033[31;1m'
white = '\033[37;1m'
yellow = '\033[33;1m'

def ulang():
	p = raw_input("Tekan enter untuk mengulang")
		
def menu():

	print "\033[32;1m   ___      ___    ___    _  __ "
	print "\033[32;1m  / __|    | __|  | _ \  | |/ / "
	print "\033[32;1m ( (__     | _|   |   /  | ' <  "
	print "\033[32;1m  \___|    |_|    |_|_\  |_|\_\ "
	print "\033[36;1m_|`````|_|`````|_|`````|_|`````|"
	print "\033[36;1m-`-0-0-'-`-0-0-'-`-0-0-'-`-0-0-'"
	print "\033[32;1mcelcius | \033[33;1mfarenheit | \033[32;1mreamur | \033[34;1mkelvin"
	print ""

	sleep(0.7)

	print "\033[31;1mTools		: \033[37;1mPerbandingan suhu"
	sleep(0.7)
	print "\033[33;1mAuthor		: \033[37;1mMaulanaRyM "
	sleep(0.7)
	print "\033[32;1mGithub		: \033[37;1mhttps://github.com/MaulanaRyM\n\n"
	sleep(0.7)
	print "\033[35;1mPilih Perbandingan"
	print "\033[31;1m[1] Celcius"
	print "\033[33;1m[2] Fahrenheit"
	print "\033[32;1m[3] Reamur"
	print "\033[34;1m[4] Kelvin"
	print "\033[37;1m[0] Keluar"
	pilih = input("\033[36;1mmasukkan pilihan: ")
	
	if pilih is 1:
		c1 = input("masukkan nilai-->")
		c = c1
		f = c1*1.8 + 32
		k = c1 + 273,5
		r = c1 * 0.8
		print """
 ########################################
 # Celcius	=	{}		#
 # Fahrenheit	=	{}		#
 # Kelvin	=	{}	#
 # Reamur	=	{}		#
 ########################################
 """.format(c, f, k, r)
	if pilih is 2:
		f1 = input("masukkan nilai-->")
		f = f1
		c = (((f1-32)*5)/9)
		k = (((f1+459.67)*5)/9)
		r = (((f1-32)*4)/9)
		print """
 ########################################
 # Celcius	=	{}		#
 # Fahrenheit	=	{}		#
 # Kelvin	=	{}		#
 # Reamur	=	{}		#
 ########################################
 """.format(c, f, k, r)
	if pilih is 3:
		r1 = input("masukkan nilai-->")
		c = ((r1*5)/4)
		f = (((r1*9)/4)+32)
		k = (((r1*5)/4)+273)
		r = r1
		print """
 ########################################
 # Celcius	=	{}		#
 # Fahrenheit	=	{}		#
 # Kelvin	=	{}		#
 # Reamur	=	{}		#
 ########################################
 """.format(c, f, k, r)
 	if pilih is 4:
		k1 = input("masukkan nilai-->")
		c = (((k1-273.15)*5)/5)
		f = (((k1*9)/5)-459.67)
		k = k1
		r = (((k1-273.15)*4)/5)
		print """
 ########################################
 # Celcius	=	{}		#
 # Fahrenheit	=	{}		#
 # Kelvin	=	{}		#
 # Reamur	=	{}		#
 ########################################
 """.format(c, f, k, r)
 

menu()
ulang()
while True:
	os.system('clear')
	menu()
	ulang()
		
