# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import redis
import hashlib

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
	db=Constants.REDIS_DB_QUESTION
	)
instance = redis.Redis(connection_pool=pool)
questionInstance = redis.Redis(connection_pool=questionPool)
checkInstance = redis.Redis(connection_pool=checkPool)
def saveQuestion(token, li):
	questionList = list(li).reverse()
	for item in questionList:
		questionInstance.lpush(token, item)

def getQuestion(token):
	questionList = questionInstance.lrange(token, 0, -1)
	return questionList

def getCheck(token):
	checkList = checkInstance.lrange(token, 0, -1)
	return checkList

def getGrade(token):
	correct = instance.hmget(Constants.CORRECT, token)
	return correct

def saveGrade(token, correct):
	instance.hset(Constants.CORRECT, token, correct)

def saveCheck(token, result):
	checkInstance.lpush(token)


