import json
import smtplib
import time
from pushbullet import Pushbullet
from craigslist import CraigslistForSale

api_key='o.'
pb= Pushbullet(api_key)
my_channel=pb.channels[0]
postlist=[]

def sendmsg(pb,result):
	msg=result['name'] + ' costs ' + result['price']+' posted on ' + result['datetime'] 
	push=pb.push_link(str(msg),str(result['url']))
	push1=my_channel.push_link(str(msg),str(result['url']))
	print "Message sent!"
	print push

while True:
	try:
		json_data=open('bikelist.json').read()
		data = json.loads(json_data)
		for post in data:
			postlist.append(post)
	except:
		print "first run"

	#craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':15, 'has_image':True}	)
	craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':16, 'has_image':True, 'posted_today':True}	)
	results=craig.get_results(sort_by='newest',limit=30)

	for result in results:
		comp=False
		loc=False
		#print result
		for item in postlist:
			if (item['url'] == result['url']):
				comp=True
				break
		print result['where']
		if result['where']!=None:
			if (result['where'].find('Raleigh')>0):
				loc=True
		if((comp==False) and ( (result['where']=='Raleigh/Cary Crossroads Cary Area') or (result['where']=='Raleigh') or ( loc==True  ))):
			postlist.append(result)
			sendmsg(pb,result)
			print result

	with open('bikelist.json', 'w') as outfile:
		jstring=json.dumps(postlist)
		outfile.write(jstring)
	time.sleep(8*3600)
