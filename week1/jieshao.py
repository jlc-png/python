c = ""
city = input("城市名（英语）：")
contry = input("国家名（英语）：")
s = input("写入景点（英语）")
if s != "finish":
    bala = input("If you want to exit, please write(finish)OK?(Yes/No)")
    if bala == "Yes":
        while True:
            chioce = input("写入景点:")
            if chioce != "finish":c = c + ", "+chioce
            if chioce == "finish":break
        print("Welcome to the city of "+city+", "+contry+".\nThere are many attractions to see, such as "+s+c+".")
    else:
        print("byebye!!!")
else:
    print(city+" no welcoms you!!!get away from here!!!(you're welcome)")