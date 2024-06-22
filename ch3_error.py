# error

# 1. IndexError  索引相關的錯誤
list = [1, 2, 3, 4, 5]
print(list[5])

# 3. TypeError   資料型態相關的錯誤
num = 5
for i in num:
    print(i)

my_list = [1, 2, 3, 4, 5]
my_list += 1

# 2. SyntaxError 語法相關的錯誤

my_list = [1, 2, 3, 4, 5

# try except
ramen_ingrediants = ("麵條", "高湯", "蔬菜", "叉燒", "糖心蛋")

try:
    ramen_ingrediants.append("芋頭")
except TypeError as e:
    print(e)
    print("拉麵放芋頭是什麼邪惡的組合？？？？")
    print("tuple 是不可變的資料型態，所以不能使用 append() 來新增值")



