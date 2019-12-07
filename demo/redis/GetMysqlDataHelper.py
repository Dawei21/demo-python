# -*- coding: UTF-8 -*-


import MySQLdb

host_value = "127.0.0.1"
user_value = "root"
pass_value = "123456"
port_value = 3306


url = 'https://'


# create triggers for mipub_gossip

def getHistoryAuthData():
	output = open('/home/sinbad/work/workspace/temp/vip_user_board_group.txt', 'w')

	db = MySQLdb.connect(user=user_value, host=host_value, passwd=pass_value, port=port_value, db="vip", charset='utf8')

	cursor = db.cursor()

	try:
		cursor.execute("select user_id, board_id from vip_user_board_group  where group_id = 1 and valid = 1")
		# 提交到数据库执行
		db.commit()
		res = cursor.fetchall()
		for row in res:
			index = 0
			for val in row:
				index = index + 1
				if index > 1:
					output.write(",")
				output.write(str(val))
				output.write("\n")
	except:
		db.rollback
	cursor.close()
	db.close()
	output.close()
	print("Finish")
	return

getHistoryAuthData()

##fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
##fetchall():接收全部的返回结果行.
##rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。