# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from flask import request,g
import jwt
from flask_restful import abort
from App.api.rest.base import BaseResource, SecureResource, rest_resource
from App.api.utils.TestCommon import TestCommon
import App.api.utils.Constants as Constants
import hashlib
import datetime
import time

from App import app

@rest_resource
class Start(BaseResource):
	""" /api/start """
	endpoints = ['/start']

	def post(self):
		jsonPayload = request.json
		difficulty = jsonPayload['difficulty']
		randomID = jsonPayload['randomID']
		typ = jsonPayload['typ']
		#token = request.headers['X-Forwarded-For']
		#token is ip
		ip = request.remote_addr
		length = jsonPayload['length']
		name = jsonPayload['name']
		'''
			TODO
			从redis中获取ip信息映射,

		''' 
		exp = datetime.datetime.utcnow() + datetime.timedelta(hours=app.config['SECURITY_TOKEN_USER_HOUR'])
		token = hashlib.md5((ip+randomID).encode('utf8')).hexdigest()
		encode = jwt.encode({
			'token': token,
			'difficulty': difficulty,
			'exp': exp
		}, app.config['SECRET_KEY'], algorithm="HS256")

		#TestCommon.savePlayer(token, name)
		first = TestCommon.randomStart(token, typ, difficulty, length)
		return {
			'retCode': Constants.SUCCESS,
			'token': encode.decode('utf-8'),
			'question': first
		}


@rest_resource
class Submit(SecureResource):
	""" /api/next """
	endpoints = ['/next']

	def post(self):
		jsonPayload = request.json
		answer = jsonPayload['answer']
		_next = TestCommon.nextQuestion(answer, g)
		flag = Constants.HAVE_NEXT
		if _next ==  Constants.COMPLETE:
			flag = Constants.END
			_next = TestCommon.getResult(g)
		return {
			'retCode': Constants.SUCCESS,
			'haveNext': flag,
			'next': _next
		}


