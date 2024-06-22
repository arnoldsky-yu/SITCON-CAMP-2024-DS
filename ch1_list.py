# 前言 - 為何要學習資料結構？

# menu 豚骨拉麵 250元、醬油拉麵 230元、蝦沾麵 280元
ramen_order1 = "豚骨拉麵"
ramen_order2 = "豚骨拉麵"
ramen_order3 = "蝦沾麵"
ramen_order4 = "醬油拉麵"
ramen_order5 = "豚骨拉麵"
ramen_order6 = "蝦沾麵"
ramen_order7 = "醬油拉麵"
ramen_order8 = "豚骨拉麵"
ramen_order9 = "蝦沾麵"
ramen_order10 = "豚骨拉麵"

# --------------------------------
# List

# 使用方括號 [] 宣告一個 list

empty_list = []

ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]
ramen_price = [250, 300, 230, 280]

# 使用 list() 函數將其他資料型態轉換為 list
number_list = list(range(1, 11))

# 使用條件式
even_number_list = [i for i in range(1, 11) if i % 2 == 0]

# --------------------------------
# 使用 List 的值 - index 操控
ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]

print(ramen_menu)

# 使用索引值 (index) 取得 list 中的值
print(ramen_menu[0])
print(ramen_menu[-1])

for i in range(4):
    print(ramen_menu[i])

# --------------------------------
# 使用 List 的值 - 用 for 來取得 list 中的值
ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]

for ramen in ramen_menu:
    print(ramen)
    print(f"我要點的是 {ramen}")



# --------------------------------
# 使用 List 的值 - 用 enumerate() 取得 index 和 value
ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]

for index, ramen in enumerate(ramen_menu):
    print(index, ramen)

# --------------------------------
# 使用 List 的值 - 使用 slice 取得部分值
ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]

print(ramen_menu[0:2])
print(ramen_menu[:2])
print(ramen_menu[2:])

# --------------------------------
# 使用 List 的值 - 修改 List 中的值
ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]

ramen_menu[0] = "豚骨拉麵 250元"
ramen_menu[1] = "牡蠣拉麵 300元"

print(ramen_menu)

# --------------------------------
# 使用 method 來操作 List - part 1
ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]

# append() - 新增一個值到 list 的最後
ramen_menu.append("特製拉麵")

# insert() - 新增一個值到 list 的指定位置
ramen_menu.insert(2, "雞白湯拉麵")

# remove() - 移除 list 中的指定值
ramen_menu.remove("雞白湯拉麵")

# del - 移除 list 中的指定位置的值
del ramen_menu[4]

print(ramen_menu)

# --------------------------------
# 使用 method 來操作 List - part 2
number_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# sort() - 將 list 中的值排序
number_list.sort()

# reverse() - 將 list 中的值反轉
number_list.reverse()

# pop() - 移除 list 中的最後一個值
number_list.pop()

# copy() - 複製 list
number_list2 = number_list.copy()

# clear() - 清空 list 中的所有值
number_list.clear()

# len() - 取得 list 中的值的數量
print(len(ramen_menu))

# --------------------------------
# 二維 List

# 原本
ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]
ramen_price = [250, 300, 230, 280]

# 二維 List 是 List 中包含 List 的資料結構
ramen_menu_with_price = [ ["豚骨拉麵", 250], ["牡蠣拉麵", 300], ["鹽味醬油拉麵", 230], ["濃厚蝦沾麵", 280] ]
print(ramen_menu_with_price[0])

# 修改二維 List 中的值
ramen_menu_with_price[2][1] = 260

# --------------------------------
ramen_menu_with_price = [ ["豚骨拉麵", 250], ["牡蠣拉麵", 300], ["鹽味醬油拉麵", 230], ["濃厚蝦沾麵", 280] ]
ramen_menu_with_price_2 = ramen_menu_with_price
ramen_menu_with_price_2.append(["特製拉麵", 300])
print(ramen_menu_with_price)
print(ramen_menu_with_price_2)



# --------------------------------
# 補充

a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print(f"a: {a}")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")









