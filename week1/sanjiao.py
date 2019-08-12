import math
import ybc_box

while True:
	choose = input('选择语言/choose language(Chinese/English)')
	if ch == '中文':
		leg1 = ybc_box.enterbox('输入腿1的长度（不加单位）：')
		leg2 = ybc_box.enterbox('输入腿2的长度（不加单位）：')
		leg1 = int(leg1)
		leg2 = int(leg2)
		hypotenuse = (leg1**2 + leg2**2)**(1/2)
		#hypotenuse = math.floor(hypotenuse)
		hypotenuse = str(hypotenuse)
		ybc_box.msgbox('这个三角形的斜边是'+hypotenuse)
	if ch == 'English':
		leg1 = ybc_box.enterbox('Enter the length of leg 1 (without units):')
		leg2 = ybc_box.enterbox('Enter the length of leg 2 (without units):')
		leg1 = int(leg1)
		leg2 = int(leg2)
		hypotenuse = (leg1**2 + leg2**2)**(1/2)
		#hypotenuse = math.floor(hypotenuse)
		hypotenuse = str(hypotenuse)
		ybc_box.msgbox('The hypotenuse of this triangle is '+hypotenuse)
	if ch == '退出/Exit' or ch == None:
		break