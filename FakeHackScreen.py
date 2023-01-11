import random
from colorama import Fore
input("This is a fake hack program as it only makes you look like you're hacking.\nPress enter to start.")
while 1 != 2:
    amount = ''.join(random.sample('1234567891256789100', 3))
    nums = ''.join(random.sample('10' * 1_000, int(amount)))
    print(Fore.LIGHTGREEN_EX + nums)
