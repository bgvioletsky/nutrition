'''
Author: bgcode
Date: 2024-12-15 21:08:56
LastEditTime: 2024-12-15 21:40:40
LastEditors: bgcode
Description: 描述
FilePath: /nutrition/main/sql.py
本项目采用GPL 许可证，欢迎任何人使用、修改和分发。
'''

import sqlite3

# 连接到SQLite数据库
try:
    conn = sqlite3.connect('src/data/ex.db')
    cursor = conn.cursor()

    # 假设这是你提供的数据，实际中可能是从接口获取等情况得到
    data = {
        "list": [
            [275, "", "烧饼(加糖)", "", "", "100%", "25.9g", "1280kJ", "8.0g", "2.1g", "", "1.3g", "62.7g", "", "", "", "—", "", "0.01mg", "1.10mg", "", "51mg", "105mg", "122mg", "62.5mg", "26mg", "1.6mg", "0.36mg", "12.20μg", "0.15mg", "", "", "—", "—", "—", "—"],
            [276, "", "油饼", "", "", "100%", "24.8g", "1702kJ", "7.9g", "22.9g", "", "2.0g", "42.4g", "", "", "", "—", "0.11mg", "0.05mg", "", "", "46mg", "124mg", "106mg", "572.5mg", "13mg", "2.3mg", "0.97mg", "10.60μg", "0.27mg", "0.71mg", "", "—", "—", "—", "—"],
            [277, "", "油条", "", "", "100%", "21.8g", "1636kJ", "6.9g", "17.6g", "", "2.7g", "51.0g", "", "", "", "—", "0.01mg", "0.07mg", "0.70mg", "", "6mg", "77mg", "227mg", "585.2mg", "19mg", "1.0mg", "0.75mg", "8.60μg", "0.19mg", "0.52mg", "", "4.1%", "63.8%", "19.0%", "88.4%"],
            [278, "", "水面筋", "", "", "100%", "63.5g", "612kJ", "23.5g", "0.1g", "", "0.6g", "12.3g", "", "", "", "—", "0.10mg", "0.07mg", "1.10mg", "", "76mg", "133mg", "69mg", "15.0mg", "26mg", "4.2mg", "1.76mg", "1.00μg", "0.19mg", "0.86mg", "", "—", "—", "—", "—"],
            [279, "", "油面筋", "", "", "100%", "7.1g", "2073kJ", "26.9g", "25.1g", "", "0.5g", "40.4g", "", "", "", "—", "0.03mg", "0.05mg", "2.20mg", "", "29mg", "98mg", "45mg", "29.5mg", "40mg", "2.5mg", "2.29mg", "22.80μg", "0.50mg", "1.28mg", "", "27.7%", "18.3%", "54.0%", "100.0%"],
            [280, "", "稻米(均值)", "", "", "100%", "13.3g", "1480kJ", "7.4g", "0.8g", "", "0.6g", "77.9g", "", "", "", "—", "0.11mg", "0.05mg", "1.90mg", "", "13mg", "110mg", "103mg", "3.8mg", "34mg", "2.3mg", "1.70mg", "2.20μg", "0.30mg", "1.29mg", "", "—", "—", "—", "—"],
            [281, "", "粳米(标一)", "", "", "100%", "13.7g", "1469kJ", "7.7g", "0.6g", "", "0.6g", "77.4g", "", "", "", "—", "0.16mg", "0.08mg", "1.30mg", "", "11mg", "121mg", "97mg", "2.4mg", "34mg", "1.1mg", "1.45mg", "2.50μg", "0.19mg", "1.36mg", "", "—", "—", "—", "—"],
            [282, "", "籼米(标准)[机米]", "", "", "100%", "12.6g", "1488kJ", "7.9g", "0.6g", "", "0.6g", "78.3g", "", "", "", "—", "0.09mg", "0.04mg", "1.40mg", "", "12mg", "112mg", "109mg", "1.7mg", "28mg", "1.6mg", "1.47mg", "2.00μg", "0.29mg", "1.27mg", "", "26.2%", "39.4%", "33.1%", "98.7%"]
        ]
    }

    # 插入数据的SQL语句，按照表结构和数据里各元素对应关系来编写，此处假设表中字段名与数据里的键或位置对应
    insert_sql = '''
    INSERT INTO message (
        id,a, name, othername, englishname, Edible, water, energy, protein, fat, cholesterol, ash, cho, dietaryfiber, carotene, vitamin, a_te, thiamin, riboflavin, niacin, vitaminC, Ca, P, K, Na, Mg, Fe, Zn, Se, Cu, Mn, I, SFA, MUFA, PUFA, Total
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
    '''

    # 循环处理数据中的每个食品信息记录（对应list中的每个子列表）进行插入
    for food_info in data["list"]:
        # 将空字符串替换为下划线
        # food_info = ['_' if item == "" else item for item in food_info]
        cursor.execute(insert_sql, food_info)
        conn.commit()
except sqlite3.Error as e:
    print(f"数据库操作出错: {e}")
finally:
    # 确保最终关闭游标和连接
    if cursor:
        cursor.close()
    if conn:
        conn.close()