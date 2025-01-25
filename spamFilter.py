from cgitb import text
# from urllib import request

def isSpam(url):
    
    spam_list = ["set #1m3", "industrial thrift store"]
    
    request_url = request.urlopen(url)
    text = str(request_url.read())
    text = text.lower()

    for spam_word in spam_list:
        # print(f"DEBUG: {type(text)} {type(spam_word)}")
        if spam_word in text:
            return True
        
    # return False

# isSpam('https://cosprings.craigslist.org/mad/d/surplus-bronze-acrylic-sheets-solar/7438433887.html')

                