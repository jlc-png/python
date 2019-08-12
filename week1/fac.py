def get_number_from_user():
    while True:
        number = input('number')
        if number.isdigit():break
        else:print("only number")
    return (int(number))
def calculate(number):
    f = 1
    for i in range(1,number+1):f *= i
    return f
get_number_from_user = get_number_from_user()
f = calculate(get_number_from_user)
print(f)