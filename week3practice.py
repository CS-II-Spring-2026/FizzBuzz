
# for i in range(1,11):
#     if i % 2 == 0:
#         print(i," Even")
#     else:
#         print(i," Odd")

# x=11

# for i in range(1,11):
#     x-=1
#     print(x

fizz= 0
buzz = 0
fizzbuzz= 0
for i in range(1,101):
    if i%3 == 0 and i%5== 0:
        print('fizzbus')
        fizzbuzz = fizzbuzz +1
    elif i % 3 == 0:
        print('fiz')
        fizz += 1
    elif i % 5 == 0:
        print('bus')
        buzz+=1
    #else:
       # print(i)

print(f"Fizz: {fizz}")
print(f"Buzz: {buzz}")
print(f"Fizzbuz:{fizzbuzz}")