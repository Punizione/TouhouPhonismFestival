# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import redis
import hashlib
import App.api.utils.Constants as Constants

pool = redis.ConnectionPool(
	host=Constants.REDIS_HOST, 
	port=Constants.REDIS_PORT,
	db=Constants.REDIS_DB
	)
questionPool = redis.ConnectionPool(
	host=Constants.REDIS_HOST,
	port=Constants.REDIS_PORT,
	db=Constants.REDIS_DB_QUESTION
	)
checkPool = redis.ConnectionPool(
	host=Constants.REDIS_HOST,
	port=Constants.REDIS_PORT,
	db=Constants.REDIS_DB_CHECK
	)

rankPool = redis.ConnectionPool(
	host=Constants.REDIS_HOST,
	port=Constants.REDIS_PORT,
	db=Constants.REDIS_DB_RANK
	)

instance = redis.Redis(connection_pool=pool)
questionInstance = redis.Redis(connection_pool=questionPool)
checkInstance = redis.Redis(connection_pool=checkPool)
rankInstance = redis.Redis(connection_pool=rankPool)
def saveQuestion(token, li):
	for item in li:
		questionInstance.rpush(token, item)
	questionInstance.expire(token, 60*60)

def getQuestion(token):
	questionList = questionInstance.lrange(token, 0, -1)
	return questionList

def getCheck(token):
	checkList = checkInstance.lrange(token, 0, -1)
	return checkList

def getCorrect(token):
	correct = instance.hmget(Constants.CORRECT, token)
	return correct

def saveCorrect(token, correct):
	instance.hset(Constants.CORRECT, token, correct)

def saveCheck(token, result):
	checkInstance.rpush(token, result)


def savePlayer(token, name):
	instance.hset(Constants.PLAYER, token, name)

def getPlayer(token):
	player = instance.hget(Constants.PLAYER, token)
	return player

def saveRanking(token, difficulty):
	correct = getCorrect(token)
	player = getPlayer(token)
	# reverse command with score and member in Redis-Py
	# zadd `key` `score` `member`
	rankInstance.zadd(difficulty, player, correct)
	'''
	ranking always save top 10
	so when put 1 member into, remove 1 member
	'''
	rankInstance.zremrangebyrank(difficulty, 0, 1)

def getRanking(difficulty):
	rank = rankInstance.zrange(difficulty, 0, 10)
	result = []
	for i in rank:
		result.append({
			"name": i,
			"grade": getCorrect(i)
			})
	return result


