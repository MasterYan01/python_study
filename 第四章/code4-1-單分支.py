weather = '下雨'
if weather == '下雨':
  print('帶雨傘出門')


# if True:
#   print('哈哈哈')

# age = int(input('請輸入年齡:'))
# if age >= 18:
#   print('可以進網咖')
# else:
#   print('滾')
# print('hello')

# score = 85
# if score > 90:
#   print('A')
# elif score > 80 and score < 90:
#   print('B')
# else:
#   print('D')

# x = 5
# match x:
#   case 1:
#     print("111")
#   case 2:
#     print("222")
#   case 3:
#     print("333")
#   case _:
#     print("other")

age = input('輸入年齡')
if age.isdigit():
    age = int(age)
    if age >0 and age <=120:
      print('輸入正確')
    else:
      print('輸入錯誤')
# 從P45開始看
# https://www.bilibili.com/video/BV1eZ421b7ag?p=45&spm_id_from=pageDriver&vd_source=6d571e7c74d5b7175d1e776ab2bc8922