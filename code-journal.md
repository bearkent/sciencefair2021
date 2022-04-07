12/29/21 - Setting up VS Code and extensions. Downloaded Python 3.10.1

12/30/21 - Finishing setting up flask and github for website building, and github to prevent code loss. 
Credit to this video https://youtu.be/kng-mJJby8g to teaching me how to use and setup flask.

1/3/22 Learned how to add images to websites.

1/4/22 Learning how to use html5 and css3 to make a form to submit missed items for recovery. Learned how to get that data into the website with flask.

1/5/22 Learned how to recieve data from users.

1/14/22 Made a form using forms-wtf and bootstrap. Also set up sqlite3 as a database for easy data collection.

1/15/22 Made a function that takes the data from the database and then adds it to a webpage. Finished the code to send you to a page that has your case.

1/17/22 Setting up image recognition

1/19/22 Made design for finding the stolen object

1/20/22 Setting up the module python-craigslist to find objects under the search query of the name of the object that they entered. Using urllib to get the html for the url from the python-craigslidt file because it doesnt output the image. Choosing between beautifulsoup and lxml to parse the html to find the image link to display on the submit page. I decide to use lxml because people have said that beaultiful soup breaks more often and has more problems.

1/23/22 Setting up lxml for parsing html for image link.

1/24/22 Trying to change what I thought was a memory object was a string.

1/26/22 Realized that what I thought was a memory object was actually a elementtree object from lxml, so I changed the code, and the parser worked. Added some code to the view to add the image and craigslist url to the html.

1/27/22 Added some code in the html that pulls the image and url from craigslist. Not working yet. Also sqlite is outputting errors on "no such column: width"

1/29/22 Debbuged the sqlite error by removing some stuff in the html. Unknown why it is happening. Then fixed the loop to make the submit.html page display the items. Figured out that there is spam words that messed up search query. Then made a function that uses urllib to get the html and then look for certain spam words in it. If the spam words are in it it excludes the item.

--Essentials Complete--

 2/4/22 Used Ngrok to create a public domain. Use ngrok http https://localhost command which is usually ngrok http https://127.0.0.1:5000