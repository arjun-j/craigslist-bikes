import json
from craigslist import CraigslistForSale

postlist=[]
try:
	json_data=open('bikelist.json').read()
	data = json.loads(json_data)
	for post in data:
		postlist.append(post)
except:
	print "first run"

craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':15, 'has_image':True}	)
#craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':5, 'has_image':True, 'posted_today':True}	)
results=craig.get_results(sort_by='newest',limit=3)

for result in results:
	print result
	comp=False
	for item in postlist:
		print item['url']
		if (item['url'] == result['url']):
			comp=True
			break
	if(comp==False):
		postlist.append(result)

with open('bikelist.json', 'w') as outfile:
	jstring=json.dumps(postlist)
	outfile.write(jstring)

