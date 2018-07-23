# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

COMPLETE = 'complete'
HAVE_NEXT = 'have_next'
END = 'end'

INFO_PATH_PREFIX = os.getcwd() + '/'
INFO_PATH_SUFFIX = '.json'


MUSIC_PATH_PREFIX = os.getcwd() + '/'
MUSIC_PATH_SUFFIX = '.mp3'


MUSIC_FRAGMENT_PATH = os.getcwd() + '/'
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
	DIFFICULTY_LUNATIC: 3,
	DIFFICULTY_EXTRA: 3
}

SECOND = 1000

SUCCESS = 'success'