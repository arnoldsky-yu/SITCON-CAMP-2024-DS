import json

SITCON_ramen_menu = { "豚骨拉麵": 250, "牡蠣拉麵": 300, "鹽味醬油拉麵": 280, "濃厚蝦沾麵": 320 }

# 將 dictionary 轉換為 JSON 格式的 string
SITCON_ramen_menu_json = json.dumps(SITCON_ramen_menu)
print(f"SITCON_ramen_menu 的型別是{type(SITCON_ramen_menu)}")
print(f"SITCON_ramen_menu_json 的型別是{type(SITCON_ramen_menu_json)}")

# 將 JSON 格式的 string 轉換為 dictionary
SITCON_ramen_menu_dict = json.loads(SITCON_ramen_menu_json)
print(f"SITCON_ramen_menu_dict 的型別是{type(SITCON_ramen_menu_dict)}")






