from PIL import Image
zodiac_number = 0
def calculat_zodiac(brith_year):
	zodiac_number = brith_year%12
	return zodiac_number
def display_photo(zodiac):
	print("Displaying your "+zodiac+" self...\nOpening "+zodiac+".jpeg")
while True:
	brith_year = input("Enter your brith year: ")
	if brith_year.isdigit():
		brith_year = int(brith_year)
		break
zodiac_number = calculat_zodiac(brith_year)
print("Calculating...")
if zodiac_number == 0:
	zodiac = "Monkey"
elif zodiac_number == 1:
	zodiac = "Rooster"
elif zodiac_number == 2:
	zodiac = "Dog"
elif zodiac_number == 3:
	zodiac = "Pig"
elif zodiac_number == 4:
	zodiac = "Rat"
elif zodiac_number == 5:
	zodiac = "Oxen"
elif zodiac_number == 6:
	zodiac = "Tiger"
elif zodiac_number == 7:
	zodiac = "Rabbit"
elif zodiac_number == 8:
	zodiac = "Dragon"
elif zodiac_number == 9:
	zodiac = "Snake"
elif zodiac_number == 10:
	zodiac = "Horse"
elif zodiac_number == 11:
	zodiac = "Sheep"
print("You are born in the year of the "+zodiac+" (by Solar Year calendar standards)")
photo = str(zodiac_number)+".jpeg"
im = Image.open("photos/"+photo)
im.show()