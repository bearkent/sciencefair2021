from datetime import datetime
from craigslist import CraigslistForSale
from imageGetter import imageGetter

def craigslistGetter(item_name, date_missed):
    cl_fs = CraigslistForSale(site='cosprings', filters={"query": f"{item_name}","has_image": True}, category='')

    items_list = []
    
    for item in cl_fs.get_results(sort_by='newest', limit=10): 
        # print("ITEM:", item)  
        image_link = imageGetter(item['url'])
        # print("IMAGE LINK:", image_link)
        item_list = [item['url'], image_link, item['datetime']]
        
        items_list.append(item_list)
        # print(item_list)
        
        # return item_list
    
    return items_list
    
print(craigslistGetter('iphone', 9/10/2))