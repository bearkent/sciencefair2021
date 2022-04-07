from datetime import datetime
from craigslist import CraigslistForSale

def craigslistGetter(item_name):
    cl_fs = CraigslistForSale(site='cosprings', filters={"query": f"{item_name}","has_image": True}, category='')

    items_list = []
    
    for item in cl_fs.get_results(sort_by='newest', limit=50): 
        item_list = [item['url'], item['datetime']]
        
        items_list.append(item_list)

    return items_list

