for i in range(3):
    s = input()
    if s.isdigit():
        n = int(s) + (3-i)
    
if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)