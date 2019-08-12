f = 1
while True:
    number = input('number')
    if number.isdigit():break
    else:print("only number")
number = int(number) + 1
for i in range(1,number):f *= i
print(str(f))