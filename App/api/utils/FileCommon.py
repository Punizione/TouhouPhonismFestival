# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import os
from pydub import AudioSegment
import uuid as UUID
import base64
import App.api.utils.Constants as Constants
import random
from App.api.utils.SplitTooLongError import SplitTooLongError

class FileCommon():
	def __init__(self):
		super().__init__()

	@classmethod
	def combine(cls, typ):
		infoDict = {}
		if type(typ) == list:
			for i in typ:
				path = Constants.INFO_PATH_PREFIX + i + Constants.INFO_PATH_SUFFIX
				with open(path, 'r', encoding='utf-8') as load:
					infoDict.update(json.load(load))
		return infoDict.keys()

	@classmethod
	def gen(cls, item, difficulty):
		if type(item) == bytes:
			item = item.decode('utf8')
		path = Constants.MUSIC_PATH_PREFIX + item + Constants.MUSIC_PATH_SUFFIX
		song = AudioSegment.from_mp3(path)
		seconds = Constants.DIFFICULTY_LEVEL[difficulty] * Constants.SECOND

		length = len(song)
		if length - seconds - (2*Constants.BEGIN) < 0:
			raise SplitTooLongError(item)

		begin = random.randint(Constants.BEGIN, length-seconds-Constants.BEGIN)
		fragment = song[begin:begin+seconds]
		if difficulty == Constants.DIFFICULTY_EXTRA:
			fragment = fragment.reverse()
		name = base64.urlsafe_b64encode(UUID.uuid4().bytes)[:-2].decode('utf-8')
		fragment.export(Constants.MUSIC_FRAGMENT_PATH+name+Constants.MUSIC_FILE_FORMAT, format="mp3")
		return name




