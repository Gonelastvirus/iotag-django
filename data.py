import json
import requests
import redis
import websocket
import random 
import time
ws=websocket.WebSocket()
ws.connect('ws://127.0.0.1:8000//ws/polData')

for i in range(1000):
	time.sleep(2)
	ws.send(json.dumps({'value':random.randint(100,500)}))
