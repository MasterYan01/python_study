# 1.3 編寫第1個程式
# ---------------------
# 注釋

# 作用：
# 方便閱讀代碼時，能夠快速的了解代碼的功能，不會被執行。

# 分類：
# 1. 塊注釋
# 2. 行內注釋
# 3. 多行注釋

# 使用規範：
# 1. 注釋不是越多越好，對於一目了然的代碼，不需要添加注釋
# 2. 對於複雜的操作，應該在操作開始前寫上若干行注釋
# 3. 對於不是一目了然的代碼，應在其行尾添加注釋
# 4. 絕不要描述代碼，假設閱讀代碼的人比你更懂 Python，他只是不了解你的代碼要做什麼

# 範例

# 塊注釋
# 以下函數用於計算兩數之和
def add(a, b):
    return a + b

# 行內注釋
result = add(2, 3)  # 計算 2 和 3 的和

# 多行注釋
'''
以下代碼用於打印計算結果
此處的計算結果是由上面的 add 函數計算得來的
我們將結果打印到控制台
'''
year=2024
month = 6
day = 27
week = "一"
weather = "熱"
temp = 35
print(result)
print(year,'年，我要減肥',sep="",end="\n\n")
print(1,1,1,sep="")
print("今天是 %d 年 %d 月 %d 日，天氣%s氣溫%.2f" % (year,month,day,weather,temp))
# 打印單個變量
print("Hello, World!")

# 打印多個變量，使用默認分隔符空格
print("Hello", "World", 123)

# 使用自定義分隔符
print("Hello", "World", 123, sep='-')
# 使用自定義結束符
print("Hello", "World", 123, end='!!!\n')

name = "Alice"
age = 30
height = 1.75

# 使用 % 格式化
print("姓名: %s, 年齡: %d, 身高: %.2f" % (name, age, height))

# 今天學到第10集
# https://www.bilibili.com/video/BV1eZ421b7ag?p=11&spm_id_from=pageDriver&vd_source=6d571e7c74d5b7175d1e776ab2bc8922