import json
import smtplib
import time
from craigslist import CraigslistForSale

def sendmsg(server,result):
	number='<number>@tmomail.net'
	msg=result['name'] + ' costs ' + result['price']+' posted on ' + result['datetime'] + 'url:  '+result['url']
	server.sendmail( '<from>', str(number), str(msg) )

postlist=[]
server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login( '<gmail_address>', '<gmail_password>' )

try:
	json_data=open('bikelist.json').read()
	data = json.loads(json_data)
	for post in data:
		postlist.append(post)
except:
	print "first run"

craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':15, 'has_image':True}	)
#craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':5, 'has_image':True, 'posted_today':True}	)
results=craig.get_results(sort_by='newest',limit=18)

for result in results:
	comp=False
	#print result
	for item in postlist:
		if (item['url'] == result['url']):
			comp=True
			break
	print result['where']
	if((comp==False) and (result['where']=='Raleigh')):
		postlist.append(result)
		print result

with open('bikelist.json', 'w') as outfile:
	jstring=json.dumps(postlist)
	outfile.write(jstring)
#time.sleep(5*3600)
