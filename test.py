# from datetime import date
#
# now = date.today()
# print(now)
# date = now.strftime("%Y-%m-%d. %d %b %Y is a %A on the %d day of %B.")
# print(date)

# import zlib
#
# s = b'witch which has which witches wrist watch'
# print(len(s))
# print(len(zlib.compress(s)))
# print(zlib.decompress(zlib.compress(s)))
# print(zlib.crc32(s))

# 平方根
# num = float(input('输入一个数字：'))
# num_sqrt = num ** 0.5
# print('%0.3f的平方根为：%0.3f' % (num, num_sqrt))
# print('{0:0.3f}的平方根为:{1:0.3f}'.format(num, num_sqrt))
# import cmath
#
# num = int(input('请输入一个数字:'))
# num_sqrt = cmath.sqrt(num)
# print('{0}的平方根为{1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))

# import cmath
#
# a = float(input('输入a:'))
# b = float(input('输入b:'))
# c = float(input('输入c:'))
#
# d = (b ** 2) - (4 * a * c)
# sol1 = (-b - cmath.sqrt(d)) / (2 * a)
# sol2 = (-b + cmath.sqrt(d)) / (2 * a)
#
# print('结果为{0}和{1}'.format(sol1, sol2))

# a = float(input('边长：'))
# b = float(input('边长：'))
# c = float(input('边长：'))
#
# s = (a + b + c) / 2
# area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
# print('三角形面积为：%0.2f' % area)

# import random
#
# print(random.randint(0, 9))

# celsius = float(input('输入摄氏温度:'))
# fahrenheit = (celsius * 1.8) + 32
# print('%0.1f摄氏温度转为华氏温度为%0.1f' % (celsius, fahrenheit))

# x = input('输入x的值：')
# y = input('输入y的值：')
#
# x, y = y, x
# print('交换后x的值为:{}'.format(x))
# print('交换后y的值为:{}'.format(y))

# num = float(input('输入一个数字:'))
# while num:
#     if num > 0:
#         print('正数')
#     elif num == 0:
#         print('零')
#     elif num < 0:
#         print('负数')
#     else:
#         break
#     num = float(input('输入一个数字:'))

# num = int(input('输入一个数字:'))
# if num % 2 == 0:
#     print('{0}是偶数'.format(num))
# else:
#     print('{0}是奇数'.format(num))

# year = int(input('请输入年份:'))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print('{0}是闰年'.format(year))
#         else:
#             print('{0}不是闰年'.format(year))
#     else:
#         print('{0}是闰年'.format(year))
# else:
#     print('{0}不是闰年'.format(year))

# num = int(input('请输入一个数字:'))
# factorial = 1
#
# if num < 0:
#     print('抱歉，负数么有阶乘')
# elif num == 0:
#     print('0的阶乘为1')
# else:
#     for i in range(1, num + 1):
#         factorial *= i
#     print('%d的阶乘为%d' % (num, factorial))

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('{}*{}={}\t'.format(i, j, i * j), end='')
#     print()

# 日历
# import calendar
#
# yy = int(input('输入年份：'))
# mm = int(input('输入月份: '))
# print(calendar.month(yy, mm))

# with open('test.txt', 'wt', encoding='utf-8') as out_file:
#     out_file.write('第一行\n第二行')
# with open('test.txt', 'rt', encoding='utf-8') as in_file:
#     text = in_file.read()
# print(text)

