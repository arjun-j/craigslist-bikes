import json
from craigslist import CraigslistForSale


craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':15, 'has_image':True}	)
#craig = CraigslistForSale(site='raleigh',category='bia',filters={ 'max_price':60, 'min_price':5, 'has_image':True, 'posted_today':True}	)
results=craig.get_results(sort_by='newest',limit=3)
postlist=[]
for result in results:
	print result
	postlist.append(result)
with open('bikelist.txt', 'a') as outfile:
	json.dumps(postlist, outfile)



json_data=open('bikelist.txt').read()

data = json.loads(json_data)
