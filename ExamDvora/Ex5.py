def defaultParameters1(x=1 ,y=2 ,z=3):
    print(x,y,z)

def defaultParameters2(x ,y=2 ,z=3):
    print(x,y,z)

def defaultParameters3(x=1, y=3, z):
    print(x, y, z)


defaultParameters1()			#1
defaultParameters1(10)			#2
defaultParameters1(10, 20)		#3
defaultParameters1(10, 20, 30)	#4

defaultParameters2()			#5
defaultParameters2(10)			#6
defaultParameters2(10, 20)		#7
defaultParameters2(10, 20, 30)	#8

defaultParameters3()			#9
defaultParameters3(10)			#10
defaultParameters3(10, 20) 		#11
defaultParameters3(10, 20, 30)	#12
