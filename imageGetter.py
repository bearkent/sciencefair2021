from lxml import html
import requests
#from lxml import etree

# tree = lxml.html.parse(StringIO("https://cosprings.craigslist.org/tag/d/colorado-springs-funko-pop-lot/7437987685.html"))

def imageGetter(link):  
    page = requests.get(f"{link}")
    tree = html.fromstring(page.content)

    images = tree.xpath("//img/@src")
    # print("DEBUG:", images)

    return images[0]

# root = tree.getroot()

# for elem in root.iter():
#     print(elem.tag)



# print(f"DEBUG 1")
# request_url = urllib.request.urlopen('https://cosprings.craigslist.org/ele/d/colorado-springs-65-inch-sharp-tv/7435512971.html')
# print(f"DEBUG 2")
# html = request_url.read()
# print(f"DEBUG 3")

# tree = etree.parse(StringIO(str(html)))
# print(f"DEBUG 4")
# #etree.tostring(tree.getroot(), pretty_print=True)
# images = tree.xpath("//img/@src")
# print(f"DEBUG 5")

# print("here")
# print(images)
# print(f"DEBUG 6")



