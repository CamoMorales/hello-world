import math
import random
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
while True:
    count += 1
    myNumber = (smaller + larger) //2
    print('%d %d' % (smaller, larger))
    print('Your number is %d' % myNumber)
    choice = input('Enter =, <, or >: ')
    if choice == '=':
        print("Yes! I got it %d tries" % count)
        break
    elif smaller == larger:
        print("I don't know, you win!")
        break
    elif choice == '<':
        larger = myNumber - 1
    else:
        smaller = myNumber + 1
        
