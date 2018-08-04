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
checkPool =redis.ConnectionPool(
	host=Constants.REDIS_HOST,
	port=Constants.REDIS_PORT,
	db=Constants.REDIS_DB_CHECK
	)
instance = redis.Redis(connection_pool=pool)
questionInstance = redis.Redis(connection_pool=questionPool)
checkInstance = redis.Redis(connection_pool=checkPool)
def saveQuestion(token, li):
	for item in li:
		questionInstance.rpush(token, item)
	questionInstance.expire(token, 60*40)

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

def saveRanking(token):
	pass

