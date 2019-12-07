# -*- coding: UTF-8 -*-

import redis


def getRedisDate():
	board_list = ['1', '2', '3']
	print('Finish')
	strict_redis = redis.StrictRedis(host = '127.0.0.1', port = '6379', db = '1')
	output = open('D:/workspace/temp/output.txt', 'w')
	print(strict_redis.ping())
	index_num = 0
	for boardId in board_list:
		index_num += 1
		cache_key = 'redisKey:%s' % boardId
		get = strict_redis.get(cache_key)
		if index_num > 1:
			output.write(",")
		output.write(str(get))
		output.write("\n")
		print(get, index_num)

	output.close()
	print('Finish')
getRedisDate()