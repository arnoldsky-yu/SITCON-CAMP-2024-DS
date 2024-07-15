# 創建 dictionary
profile = {
  "綽號": "Arnoldsky",
  "就讀科系": "中原資工系大四",
  "社群經驗": ["SITCON", "HITCON"],
  "目前學習": ["AI", "雲端"],
  "興趣": ["遊戲", "閱讀", "聽音樂劇"],
}

print(profile)
print(profile["綽號"])

profile2 = dict(
    綽號="Arnoldsky",
    就讀科系="中原資工系大四",
    社群經驗=["SITCON", "HITCON"],
    目前學習=["AI", "雲端"],
    興趣=["遊戲", "閱讀", "聽音樂劇"]
)

# --------------------------------
profile = {
  "綽號": "Arnoldsky",
  "就讀科系": "中原資工系大四",
  "社群經驗": ["SITCON", "HITCON"],
  "目前學習": ["AI", "雲端"],
  "興趣": ["遊戲", "閱讀", "聽音樂劇"],
}

# 新增 dictionary - 1
profile["薪水"] = 0

# 新增 dictionary - 2
profile.update({"年齡": 21})

# 修改 dictionary - 1
profile["綽號"] = "Arnold"

# 修改 dictionary - 2
profile.update({"綽號": "Arnoldsky"})

# 修改 dictionary - 3
profile["社群經驗"].append("COSCUP")

profile["目前學習"] = ["AI", "雲端", "資安"]

# 刪除 dictionary - 1
del profile["興趣"]

# 刪除 dictionary - 2
major = profile.pop("就讀科系")

# --------------------------------
# 使用 method 來操作 dictionary

# get value
value = profile.values()
print(value)

for value in profile.values():
    print(value)

# get key
key = profile.keys()
print(key)

for key in profile.keys():
    print(key)

# get items
items = profile.items()
ZW
for key, value in items:
    print(f'key 是 {key},   value 是 {value}')

# --------------------------------
# Key 值是否存在於 dictionary 中

# in
if "綽號" in profile:
    print("綽號 存在於 profile 中")

# not in
if "年齡" not in profile:
    print("年齡 不存在於 profile 中")

# --------------------------------
# 題目數據 - part 1
profileList = [{"name": "Arnoldsky","age": "21",}, {"name": "John","age": "22",}, {"name": "Mary", "age": "20",},{"name": "Tom", "age": "23",}, 
                {"name": "Jerry", "age": "24",}, {"name": "Marry", "age": "25",}, {"name": "Tony", "age": "22",}, {"name": "Tina", "age": "21",}, 
                {"name": "Jenny", "age": "20",}, {"name": "Jack", "age": "27",}, {"name": "Rose", "age": "26",}, {"name": "David", "age": "28",},
                {"name": "Doris", "age": "19",}, {"name": "Daisy", "age": "25",}, {"name": "Duke", "age": "24",}, {"name": "Dora", "age": "27",},]

# 題目數據 - part 2
paragraph = '''Spinoza published little to avoid persecution and bans on his books. 
In his Tractatus Theologico-Politicus, described by Steven Nadler as \"one of the most important books of Western thought\", 
Spinoza questioned the divine origin of the Hebrew Bible and the nature of God while arguing that ecclesiastic authority should have no role in a secular, democratic state. 
Ethics argues for a pantheistic view of God and explores the place of human freedom in a world devoid of theological, cosmological, and political moorings. 
Rejecting messianism and the emphasis on the afterlife, Spinoza emphasized appreciating and valuing life for ourselves and others. 
By advocating for individual liberty in its moral, psychological, and metaphysical dimensions, Spinoza helped establish the genre of political writing called secular theology.'''