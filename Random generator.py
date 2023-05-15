#IDK what this is:

import os
import random

print("\nWelcome to Some weired ass random python program:\n")
print('''
So basically enter the number of choices, Then enter the choices and this
program will randomly select of the options for you!!
''')
size=int(input("Enter the Number of choices :\t"))
i=1
options=[ ]
while(i<=size):
    options.append(str(input("Enter the choice "+ str(i) +":\t")))
    i+=1
output = random.choice(options)
print("\nSO The Best choice from the above according to computer is:")
print(output)



