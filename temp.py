import json

with open ('channel_messages.json') as f:
	messages_json = json.load(f)

for i in range(len(messages_json)-1):
	try:
		print(f'number {i}')
		print(messages_json[i]['message'])
	except:
		pass

