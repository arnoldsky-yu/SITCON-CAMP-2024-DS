# tuple 
ramen_ingrediants = ("麵條", "高湯", "蔬菜", "叉燒", "糖心蛋")

# 用 len() 取得 tuple 的長度
print(len(ramen_ingrediants))

# 用 index() 取得 tuple 中的值的索引值
print(ramen_ingrediants[0])

# unpacking
noodle, soup, vegetable, pork, egg = ramen_ingrediants

# 用 + 來合併 tuple
ramen_ingrediants = ramen_ingrediants + ("叉燒飯", "可樂")

# 用 for 迴圈來取得 tuple 中的值
for ingrediant in ramen_ingrediants:
    print(ingrediant)
    

# --------------------------------

# 修改 tuple 中的值
ramen_ingrediants[0] = "烏龍麵"

ramen_ingrediants.append("芋頭")

ramen_ingrediants.remove("蔬菜")





