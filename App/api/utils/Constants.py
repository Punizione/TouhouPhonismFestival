# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

COMPLETE = 'complete'
HAVE_NEXT = True
END = False

SUCCESS = 'success'
EXPIRED = 'expired'
INFO_PATH_PREFIX = os.getcwd() + '\\' + 'App\\conf' + '\\'
INFO_PATH_SUFFIX = '.json'


MUSIC_PATH_PREFIX = os.getcwd() + '\\' + 'App\\music' + '\\'
MUSIC_PATH_SUFFIX = '.mp3'


MUSIC_FRAGMENT_PATH = os.getcwd() + '\\' + 'App\\temp' + '\\'
MUSIC_FILE_FORMAT = '.mp3'

BEGIN = 5000


DIFFICULTY_EASY = 'easy'
DIFFICULTY_NORMAL = 'normal'
DIFFICULTY_HARD = 'hard'
DIFFICULTY_LUNATIC = 'lunatic'
DIFFICULTY_EXTRA = 'extra'



DIFFICULTY_LEVEL = {
	DIFFICULTY_EASY: 10,
	DIFFICULTY_NORMAL: 7,
	DIFFICULTY_HARD: 5,
	DIFFICULTY_LUNATIC: 2,
	DIFFICULTY_EXTRA: 5
}

SECOND = 1000


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_DB_QUESTION = 1
REDIS_DB_CHECK = 2

CORRECT = 'correct'
