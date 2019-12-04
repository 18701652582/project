#encoding:utf-8
'''
@projrct = project
@file = 01
@author = Administrator
@create_time = 2019/10/24 10:07
'''
# vim randpass.py
#!/usr/bin/python
import string
import random
#获取随机的字母
s = string.ascii_letters
r = random.choice(s)
#print(r)
#获取一个1-10000内的随机整数
num = random.randint(1,10000)

print(num)
passwd = ''
passchs = str(r) + str(num)
for i in range(8):
	passwd += random.choice(passchs)
print(passwd)