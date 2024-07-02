# n = 0
# while n<5:
#   print('hello python')
#   n += 1
#   print(n)

# n = 1
# result = 0
# while n < 1000:
#   result += n
#   n+= 1
# print(result)
# while '111':
#   print(1)

# reslut2 = 0
# n = 1
# while n<=4:
#   reslut = 1
#   m = 1
#   while m<=n:
#     reslut *= m
#     m += 1
#   reslut2 += reslut
#   n +=1
# print(reslut2)

# n = 5
# for i in range(2,n):
#   if n%i==0:
#     print(n,'不是質數')
#     break
# else:
#   print(n,'是質數')

# 人生複利
# year = 0
# total = 1
# while year <10:
#   total = total*1.1
#   print(total)
#   year += 1




# 1×1=1
# 1×2=2  2×2=4
# 1×3=3  2×3=6  3×3=9
# 1×4=4  2×4=8  3×4=12  4×4=16
# ...
# 1×9=9  2×9=18  3×9=27  4×9=36  5×9=45  6×9=54  7×9=63  8×9=72  9×9=81
# 這段程式碼使用兩個 for 循環來生成乘法表。
# 外層循環控制乘法表的行數（從 1 到 9），
# 內層循環控制每行的內容（從 1 到當前行數）。
# print 函數的 end="\t" 參數用來在同一行輸出結果，
# 使用制表符來對齊每個乘法表的結果。
# print() 用來在每行結束後進行換行。

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={j*i}", end="\t")
    print()

#P53 從第6章開始看
# https://www.bilibili.com/video/BV1eZ421b7ag?p=53&spm_id_from=pageDriver&vd_source=6d571e7c74d5b7175d1e776ab2bc8922

