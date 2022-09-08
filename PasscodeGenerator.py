# Passcode Generator 
import random
length = int(input("Enter the length of passcode you want: "))
arbitrartvalues ='abcdefgh123456789'
passcode = "".join(random.sample(arbitrartvalues,length))
print(passcode)