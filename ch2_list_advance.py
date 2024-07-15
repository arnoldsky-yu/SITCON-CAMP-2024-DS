# 進階 List 操作
# --------------------------------
# List Comprehension
# List Comprehension 是 Python 中一個方便的功能，可以快速的建立 List。
# 語法: [expression for item in iterable if condition]

even_number_list = [i for i in range(1, 21) if i % 2 == 0]

even_number_list = []
for i in range(1, 21):
    if i % 2 == 0:
        even_number_list.append(i)

print (even_number_list)

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
# 用 zip() 來合併兩個 List

ramen_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]
ramen_price = [250, 300, 230, 280]

ramen_menu_with_price = list(zip(ramen_menu, ramen_price))
print(ramen_menu_with_price)

# --------------------------------
# 題目 參考答案
ramen_menu_with_price = [ ["豚骨拉麵", 250], ["牡蠣拉麵", 300], ["鹽味醬油拉麵", 230], ["濃厚蝦沾麵", 280] ]
ramen_menu_with_price_2 = ramen_menu_with_price
ramen_menu_with_price_2.append(["特製拉麵", 300])
print(ramen_menu_with_price)
print(ramen_menu_with_price_2)
# --------------------------------
# shallow copy & reference

a = [1, 2, 3]
b = a
c = a.copy()
b.append(4)
print(f"a: {a}")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

# --------------------------------
# packing & unpacking

# packing
ramen1 = "豚骨拉麵"
ramen2 = "牡蠣拉麵"
ramen3 = "鹽味醬油拉麵"

ramen_menu = [ramen1, ramen2, ramen3]
print(ramen_menu)

# unpacking
ramen4, ramen5, ramen6 = ramen_menu
print(ramen4)
print(ramen5)
print(ramen6)