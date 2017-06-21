#!/usr/bin/python3
from datetime import datetime
import time
import os
import random
import sys

from pyglet.gl import *
import pyglet
from pyglet.window import key

SOUNDTEST = 'good-morning.mp3'

punch = "8:30"
punch2 = "11:30"
punch3 = "12:0"
punch4 = "17:0"

def alarm():
	sound = pyglet.resource.media(SOUNDTEST, streaming=False)
	window = pyglet.window.Window(width=920, height=640)
	image = pyglet.resource.image('vader_business.jpg')
	label = pyglet.text.Label('Punch!',
								font_name='Times New Roman',
								font_size=36,
								x = window.width//2,
								y = window.height//2,
								anchor_x='center', anchor_y='center')
	@window.event

	def on_draw():
		window.clear()
		image.blit(0,0)
		label.draw()
		sound.play()
	pyglet.app.run()
	return;

while True:
	dayNumber = datetime.today().weekday()
	now = datetime.now()
	nowformat = '%s:%s' % (now.hour, now.minute)

	if dayNumber == 5: # if dayNumber == Saturday
		time.sleep(172800) # 2 days
	else:
		if nowformat == punch:
			alarm()
			time.sleep(10740) # 2.98 hours
			pass
		elif nowformat == punch2:
			alarm()
			time.sleep(1620) # 27 mins
			pass
		elif nowformat == punch3:
			alarm()
			time.sleep(17640) # 4.9 hours
			pass
		elif nowformat == punch4:
			alarm()
			time.sleep(55200) # 15.33 hours
			pass
		else:
			time.sleep(5) # 5 seconds
