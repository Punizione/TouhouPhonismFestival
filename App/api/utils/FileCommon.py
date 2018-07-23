# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os
from pydub import AudioSegment
import uuid as UUID
import base64
import Constants
class FileCommon(Object):
	def __init__(self):
		super().__init__()

	@class_method
	def combine(typ):
		infoDict = {}
		if type(typ) == list:
			for i in typ:
				path = Constants.INFO_PATH_PREFIX + i + Constants.INFO_PATH_SUFFIX
				with open(path, 'r', encoding='utf-8') as load:
					infoDict.update(json.load(load))
		return infoDict.keys()

	@class_method
	def gen(item, difficulty):
		path = Constants.MUSIC_PATH_PREFIX + item + Constants.MUSIC_PATH_SUFFIX
		song = AudioSegment.from_mp3(item)
		seconds = Constants.DIFFICULTY_LEVEL[difficulty] * Constants.SECOND

		length = len(song)
		if length - seconds - (2*Constants.BEGIN) < 0:
			raise SplitTooLongException(item)

		begin = random.randint(Constants.BEGIN, length-seconds-Constants.BEGIN)
		fragment = song[begin:begin+seconds]
		if difficulty == Constants.DIFFICULTY_EXTRA:
			fragment = fragment.reverse()
		name = base64.urlsafe_b64encode(UUID.uuid4().bytes)[:-2].encode('utf-8')
		fragment.export(Constants.MUSIC_FRAGMENT_PATH+name+Constants.MUSIC_FILE_FORMAT, format="mp3")
		return name




