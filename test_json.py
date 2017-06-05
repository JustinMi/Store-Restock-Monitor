import json

JSON_FILE = 'WebsiteStates.json'

with open(JSON_FILE, 'w') as savefile:
	json.dump("hi", savefile, indent=4, separators=(',', ':'))

with open(JSON_FILE, 'w') as savefile:
	json.dump("bye", savefile, indent=4, separators=(',', ':'))