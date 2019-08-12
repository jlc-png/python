choose = input('选择语言/choose language(Chinese/English)')
if choose == 'Chinese':
	name = input('你的名字是什么？')
	sex = input('你的性别是什么？，男or女？')
	age = input('你几岁了？')
	age = int(age) + 10
	age = str(age)
	if sex == '男':
		print('你好，',name,'男士，你在2029年时是',age,'岁')
	if sex == '女':
		print('你好，',name,'女士，你在2029年时是',age,'岁')
if choose == 'English':
	name = input("What's your name？")
	sex = input("What's your gender? , male or female？")
	age = input('How old are you？')
	age = int(age) + 10
	age = str(age)
	if sex == 'male':
		print('Hello，Sir',name,',You will be',age,'years old in 2029.')
	if sex == 'female':
		print('Hello，Madame',name,',You will be',age,'years old in 2029.')