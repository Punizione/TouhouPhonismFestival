# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from App.api.utils.FileCommon import FileCommon
import App.api.utils.RedisCommon as RedisCommon
import App.api.utils.Constants as Constants
class TestCommon():
	def __init__(self):
		super().__init__()


	@classmethod
	def randomStart(cls, token, typ, difficulty, length):
		li = cls.genQuestionList(typ, length)
		"""
		保存li内容到redis
		"""
		RedisCommon.saveQuestion(token, li)
		return FileCommon.gen(li[0], difficulty)

	@classmethod
	def nextQuestion(cls, answer, g):
		token = g.token
		difficulty = g.difficulty
		"""
		从redis中取出余下问题链接和答案结果链接
		"""
		questionList = RedisCommon.getQuestion(token)
		correct = RedisCommon.getCorrect(token)
		checkList = RedisCommon.getCheck(token)

		result = cls.check(questionList[len(checkList)], answer)
		if result:
			correct += 1
			"""
				保存分数，答对题数
			"""
			RedisCommon.saveCorrect(token, correct)

		"""
			答题内容
		"""
		RedisCommon.saveCheck(token, answer)
		print('%d-%d' %(len(checkList), len(questionList)))
		if len(checkList) == len(questionList)-1:
			return Constants.COMPLETE
		return FileCommon.gen(questionList[len(checkList)+1], difficulty)


	@classmethod
	def getResult(cls, g):
		token = g.token
		difficulty = g.difficulty
		"""
			从redis中取出所有问题链接和答案结果链接与评分
		"""
		questionList = RedisCommon.getQuestion(token)
		correct = RedisCommon.getCorrect(token)
		checkList = RedisCommon.getCheck(token)

		RedisCommon.saveRanking(token, difficulty)
		if len(questionList) >=50:
			saveRank(token, difficulty)
		retList = []
		for i in range(len(questionList)):
			retList.append({
				"q": questionList[i].decode('utf8'),
				"a": checkList[i].decode('utf8')
			})
		return {
			"data": retList
		}

	@classmethod
	def check(cls, question, answer):
		return question == answer


	@classmethod
	def genQuestionList(cls, typ, length):
		return random.sample(FileCommon.combine(typ), length)


	@classmethod
	def savePlayer(cls, token, name):
		RedisCommon.savePlayer(token, name)

	@classmethod
	def getRank(cls, difficulty):
		return RedisCommon.getRanking(difficulty)

	@classmethid
	def saveRank(cls, token, difficulty):
		RedisCommon.saveRank(token, difficulty)



