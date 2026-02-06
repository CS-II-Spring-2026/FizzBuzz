fizz = 0
buzz = 0
fizzbuzz = 0

for i in range (1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "Fizz Buzz")
        fizzbuzz = fizzbuzz + 1
    elif i % 3 == 0: 
        print(i, "Fizz")
        fizz+= 1
    elif i % 5 == 0:
        print(i, "Buzz")
        buzz+=1
    else:
        print (i)

print(f"Fizz: {fizz}")
print(f"Buzz: {buzz}")
print(f"FizzBuzz: {fizzbuzz}")

