#encoding:utf-8
'''
@projrct = project
@file = selectData
@author = Administrator
@create_time = 2019/6/18 14:45
'''
'''
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
fetchall(): 接收全部的返回结果行.
rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "weilin", "testdb")
# 使用cursor()方法获取操作游标
cursor = db.cursor()
'''
# SQL 查询语句
sql = "SELECT * FROM EMPLOYEE WHERE INCOME > %s" % (1000)
try:
	# 执行SQL语句
	cursor.execute(sql)
	# 获取所有记录列表
	results = cursor.fetchall()
	print(results)
	#results[0][0]  #Mac
	print(results[0][0])
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		# 打印结果
		print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" %  (fname, lname, age, sex, income))
except Exception as e:
	print("Error: unable to fetch data:%s" %e)

# 关闭数据库连接
db.close()
'''

'''
try:
	cursor.execute("select * from employee")  # 执行sql
	rs1 = cursor.fetchone()  # 获取一行记录
	print(rs1) #元组
	print(len(rs1))
	print(rs1[0])#获取('Mac', 'Mohan', 21, 'M', 2000.0)中的Mac
	rs2 = cursor.fetchmany(2)  # 获取余下记录中的2行记录
	print(rs2)
	print(rs2[1][0])#获取(('Erer', 'Man', 30, 'F', 9000.0), ('Dff', 'Qt', 20, 'F', 1800.0)) 中的Dff
	ars = cursor.fetchall()  # 获取剩下的所有记录
	for rs in ars:
		print(rs)
except Exception as e:
	print("Error to select:", e)
db.close()
'''

#从数据库读取值，用于参数化。
try:
	names = []
	#获取所有的FIRST_NAME
	cursor.execute("select FIRST_NAME from employee")  # 执行sql
	ars = cursor.fetchall()  # 获取剩下的所有记录；获取结果集中的所有行
	#获取的是元组
	#print(ars)
	for rs in ars:
		#元组转化为列表；并进行拼接
		names += list(rs)
	#可以逐个读取，用于参数化。
	print(names)
except Exception as e:
	print("Error to select:", e)
db.close()

