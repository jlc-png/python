a,b = "first","second"
c,d = 0.5,1
def get_number_from_user(x):
	while True:
		number = input(x+' side: ')
		if number.isdigit():break
		else:print("only number")
	return (int(number))
def calculate_pythagorean_or_area(number1,number2,y):
	third_side = (first_side**2 + second_side**2)**y
	return third_side
first_side = get_number_from_user(a)
second_side = get_number_from_user(b)
third_side = calculate_pythagorean_or_area(first_side,second_side,c)
area = calculate_pythagorean_or_area(first_side,second_side,d)
print("From the majestic triangle of Marvel universe with sides "+str(first_side)+" and "+str(second_side)+", there lays a holy square of equal sides "+str(round(third_side,3))+" and an area of "+str(area)+".")