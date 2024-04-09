# Fizz Buzz
Write a short program that prints each number from 1 to 100 on a new line.

For each multiple of 3, print Fizz instead of the number.

For each multiple of 5, print Buzz instead of the number.

For numbers which are multiples of both 3 and 5, print Fizz Buzz instead of the number.

It should produce output like this:
```python
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
Fizz Buzz
16
...
```

# Solution
```python
for number in range(1,101): 
    if ( ((number % 3) == 0) and ((number % 5) == 0) ): # if both of these statements are true print fizz buzz
        print("fizz buzz")
    elif ((number % 3) == 0): # number is a multiple of 3
        print("fizz")
    elif ((number % 5) == 0): # number is a multiple of 5
        print("buzz")
    else: print(number) # number is not a multiple of 3 or 5
x = float(x)
y0 = float(y0)
y = (x * math.tan(theta)) - (1 / (2 * (v0**2))) * (g * (x**2) / math.cos(theta)**2) + y0
y = round(y,11)
print(f"The vertical height of the ball is: {y} m")
```
