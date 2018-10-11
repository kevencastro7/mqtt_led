#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'keven'

import os
import sys
import signal
from fase import MicroServiceBase
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import time


class Mqtt(MicroServiceBase):
    def __init__(self):
        super(Mqtt, self).__init__(self, sender_endpoint='ipc:///tmp/sender',
                                   receiver_endpoint='ipc:///tmp/receiver')
        self.topic = "topic/led"
        self.hostname = "broker.hivemq.com"
        self.attempts = 2

    def on_broadcast(self, service, data):
        pass

    def on_connect(self, client, userdata, flags, rc):
        self.client.subscribe(self.topic)

    def on_new_service(self, service, actions):
        pass

    def on_message(self, client, userdata, msg):
        print(msg.payload)

    def conectar(self):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        attempts = 0
        while attempts < self.attempts:
            try:
                self.client.connect(self.hostname, 1883, 60)
                print "deu bom"
                return True
            except:
                attempts += 1
                print "Tentativa: " + str(attempts) + " - Não foi possível conectar"
        return False

    """#############################################################################################################"""
    """################################################### TASKS  ##################################################"""
    """#############################################################################################################"""

    @MicroServiceBase.task
    def MainTask(self):
        if self.conectar():
            self.client.loop_forever()
        else:
            print "Máximo de tentativas atiginda"
            os.kill(os.getpid(), signal.SIGKILL)


Mqtt().execute(enable_tasks=True)