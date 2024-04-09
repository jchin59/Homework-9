# Sample solution for Fizz Buzz

for number in range(1,101): 
    if ( ((number % 3) == 0) and ((number % 5) == 0) ): # if both of these statements are true print fizz buzz
        print("fizz buzz")
    elif ((number % 3) == 0): # number is a multiple of 3
        print("fizz")
    elif ((number % 5) == 0): # number is a multiple of 5
        print("buzz")
    else: print(number) # number is not a multiple of 3 or 5
