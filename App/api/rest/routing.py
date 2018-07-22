# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from flask import request,g
import jwt
from flask_restful import abort
from App.api.rest.base import BaseResource, SecureResource, rest_resource
from TestCommon import TestCommon
import Constants
import hashlib

@rest_resource
class Start(BaseResource):
	""" /api/start """
	endpoints = ['/start']

	def get(self):
		difficulty = request.args.get('difficulty')
		randomID = request.args.get('random')
		#token = request.headers['X-Forwarded-For']
		#token is ip
		ip = request.remote_addr
		length = request.args.get('length')
		'''
			TODO
			从redis中获取ip信息映射,

		''' 
		exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['SECURITY_TOKEN_USER_HOUR'])
		encode = jwt.encode({
			'token': hashlib.md5(ip+randomID),
			'difficulty': difficulty,
			'exp': exp
		}, app.config['SECRET_KEY'], algorithm="HS256")


		first = TestCommon.randomStart(token, typ, difficulty, length)
		return {
			'retCode': Constants.SUCCESS,
			'token': encode,
			'question': first
		}


@rest_resource
class Submit(SecureResource):
	""" /api/next """
	endpoints = ['/next']

	def get(self):
		answer = request.args.answer
		if answer == Constants.COMPLETE:
			_next = TestCommon.getResult(g)
			flag = Constants.END
		else:
			_next = TestCommon.nextQuestion(answer, g)
			flag = Constants.HAVE_NEXT
			if _next ==  Constants.COMPLETE:
				flag = Constants.END
		return {
			'retCode': Constants.SUCCESS,
			'haveNext': flag,
			'next': _next
		}

