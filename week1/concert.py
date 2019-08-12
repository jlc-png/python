weather = input("Will it rain tonight? (Yes,No)")
is_raining_outside = weather == "No"

money = input("How much money do you have?")
money = float(money)
enough = money > 50

friends1 = input("Will Ben go with you? (Yes,No)")
friends2 = input("Will John go with you? (Yes,No)")
kkkk = friends1 == "Yes"
llll = friends2 == "Yes"
jjjj = kkkk or llll

should_go_to_concert = is_raining_outside and enough and jjjj
if should_go_to_concert == True:
 	print("Yes,you should")
if should_go_to_concert == False:
	print("No,you shouldn\'t go")