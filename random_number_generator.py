from colorama import Fore
import random
import time


while True :
	sum = random.randint(1,99999999999999999999999999999999999999999999999999999999999999999)
	
	print(Fore.GREEN + f"{sum}" + Fore.RESET)
	time.sleep(0.05)