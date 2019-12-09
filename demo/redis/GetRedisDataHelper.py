# -*- coding: UTF-8 -*-


from rediscluster import StrictRedisCluster



def getRedisDate():
	board_list = []
	print('Start ---')
	nodes = [{"host":"", "port":""}]
	strict_redis = StrictRedisCluster(startup_nodes=nodes, decode_responses=True, skip_full_coverage_check=True)
	# output = open('D:/workspace/temp/output.txt', 'w')
	print(strict_redis.ping())
	for boardId in board_list:
		cache_key = 'vip#14_Question:Send:Email:Schedule:TimePoint%s' % boardId
		get = strict_redis.get(cache_key)
		print(str(cache_key + " = " + str(get)))
		result = strict_redis.set(cache_key, "1575508917000");
		print(result)
		# if index_num > 1:
		#       output.write(",")
		# output.write(str(get))
		# output.write("\n")
		print(str(cache_key + " = " + str(get)))
	print('Finish')


getRedisDate()

getRedisDate()
