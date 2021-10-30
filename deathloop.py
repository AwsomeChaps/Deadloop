import random
import string
import math
from random import shuffle



def main():
	l=[]
	for i in range(0,100):
		l.append(i)
	done = False
	while not done:
		if (random.randint(1,100)==9):
			if (random.choice(string.ascii_letters) == 'd'):
				shuffle(l)
				if(l[0] == 7):
					if(random.randint(100,1000)+random.randint(100,1000)>1900):
						if(random.uniform(5,10)>5):
							if ('5' in str(random.randint(1,50)+random.randint(1,10))):
								if (random.randint(1,10)==random.randint(1,10)):
									if (math.sin(random.randint(-5,5))<0):
										if (random.gauss(100,50)<0):
											done = True	
	print("DONE")	



if __name__ == '__main__':
	main()