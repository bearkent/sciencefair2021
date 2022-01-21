from craigslist import CraigslistForSale
#fs means for sale
cl_fs = CraigslistForSale(site='cosprings', filters={"query": "tv","has_image": True}, category='')

for item in cl_fs.get_results(sort_by='newest', limit=10):
    print(item)
    
    #print(item['name'])
    #print(item['url']+'\n')
    
        