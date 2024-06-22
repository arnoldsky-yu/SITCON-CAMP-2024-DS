# Set(集合)
# 宣告 Set

# 宣告一個空集合
empty_set = set()
print(type(empty_set))
# 如果用 {} 呢？
empty_set = {}
print(type(empty_set))

# 宣告一個有值的集合
ramen_menu = {"豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"}

# 使用 set() 函數將其他資料型態轉換為集合
number_set = set(range(1, 11))

# --------------------------------
# 來點實際的例子
# 我們家拉麵店的拉麵口味
ramen_SITCON_menu = ["豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"]

# 另一間拉麵店的拉麵口味
ramen_another_shop_menu = ["豚骨拉麵", "鮮魚白湯拉麵", "鹽味醬油拉麵"]

# 使用 set() 來建立集合
ramen_SITCON_set = set(ramen_SITCON_menu)
ramen_another_shop_set = set(ramen_another_shop_menu)

# 使用 & 來取得兩個集合的交集
print(ramen_SITCON_set & ramen_another_shop_set)

# 使用 | 來取得兩個集合的聯集
print(ramen_SITCON_set | ramen_another_shop_set)

# 使用 - 來取得兩個集合的差集
print(ramen_SITCON_set - ramen_another_shop_set)

# --------------------------------
# Set 是沒有順序的
ramen_menu = {"豚骨拉麵", "牡蠣拉麵", "鹽味醬油拉麵", "濃厚蝦沾麵"}
ramen_menu[0] 



