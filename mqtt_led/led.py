#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'keven'

import RPi.GPIO as gpio
import time

class Led(MicroServiceBase):
	def __init__(self):
		super(Mqtt, self).__init__(self, sender_endpoint='ipc:///tmp/sender',
                                                 receiver_endpoint='ipc:///tmp/receiver')
		self.gpio.setmode(gpio.BCM)
		self.pin = 18
		self.gpio.setup(self.pin, gpio.OUT)
		

    	def on_broadcast(self, service, data):
        	pass

	def on_connect(self):
	    	pass

    	def on_new_service(self, service, actions):
        	pass
	
	def ligar(self):
		self.gpio.output(self.pin, gpio.HIGH)

	def desligar(self):
		self.gpio.output(self.pin, gpio.LOW)

    	"""#############################################################################################################"""
    	"""################################################### TASKS  ##################################################"""
    	"""#############################################################################################################"""
    	@MicroServiceBase.task
    	def MainTask(self):
        	while True:
			self.ligar()
			time.sleep(0.5)
			self.desligar
			time.sleep(0.5)


gpio().execute(enable_tasks=True)
