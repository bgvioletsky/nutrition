import requests
import sqlite3
import json
import time
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Length": "63",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "JSESSIONID=5A3C82ACF28A60CD76B637615C98B365; Hm_lvt_f1641da686b7b197f19488d93a0ff060=1734265193; Hm_lpvt_f1641da686b7b197f19488d93a0ff060=1734265193; HMACCOUNT=4296661A49C20180; acw_tc=2760820a17342676709178505e27f6d2d81048d90be4275e7db17c431c6ba9",
    "DNT": "1",
    "Host": "nlc.chinanutri.cn",
    "Origin": "https://nlc.chinanutri.cn",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"macOS\""
}
data = {
    "categoryOne": "0",
    "categoryTwo": "0",
    "foodName": "0",
    "pageNum": "0",
    "field": "0",
    "flag": "0"
}
url = "https://nlc.chinanutri.cn/fq/FoodInfoQueryAction!queryFoodInfoList.do"


def requests_post(url, headers ,data,i):
    try:
        response = requests.post(url, headers=headers, data=data)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"请求第{i}页时发生错误: {e}")
        
def parse_json(response_text):
    data=json.loads(response_text)
    try:
        conn = sqlite3.connect('src/data/foodlable.db')
        cursor = conn.cursor()
        insert_sql = '''
        INSERT INTO message (
            id,a, name, othername, englishname, Edible, water, energy, protein, fat, cholesterol, ash, cho, dietaryfiber, carotene, vitamin, a_te, thiamin, riboflavin, niacin, vitaminC, Ca, P, K, Na, Mg, Fe, Zn, Se, Cu, Mn, I, SFA, MUFA, PUFA, Total
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
        '''
        for food_info in data["list"]:
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
            
def main():
    for i in range(96, 171):
         try:
            data["pageNum"] = i
            response_text = requests_post(url, headers, data,i)
            time.sleep(10)
            parse_json(response_text)
         except requests.RequestException as e:
            print(f"请求第{i}页时发生错误: {e}")
         print(f"第{i}页已爬取完毕")
main()
print("爬取完毕")