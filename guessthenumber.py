import random
r = random.randint(1,20)

while(True):
    inp = int(input("Enter the number: "))
    if(inp<r):
        print("Wrong guess, try a greater number")
    elif(inp>r):
        print("Wrong guess, try a smaller number")
    else:
        print("Congo! Your guessing is correct")
        break;