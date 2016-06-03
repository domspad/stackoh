
import requests
import json

TAG_TEMPLATE = 'https://api.stackexchange.com/2.2/tags/{}/info?order=desc&sort=popular&site=stackoverflow'

def tag_question_count(tagname):
	"""
	If tag is unrecognized then defau
	"""
	resp = requests.get(TAG_TEMPLATE.format(tagname))
	payload = json.loads(resp.text)
	items = payload.get('items')
	if items:
		return payload['items'][0]['count']
	else:
		return 0

# TODO get fraction of questions unanswered