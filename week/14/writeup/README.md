Writeup 10 - Crypto II
=====

Name: *Travis Burk*
Section: *0201*

I pledge on my honor that I have not given or received any unauthorized assistance on this assignment or examination.

Digital acknowledgement of honor pledge: *Travis Burk*

## Assignment 10 Writeup

### Part 1 (70 Pts)
*The Flag : CMSC38R-{y0U-are_the_5ql_n1nja}*
*My first step towards finding this flag was viewing all the pages on the website. After several looks I found that the linked pages found on the table all had a similar url, that had a id value attached to the end "cornerstoneairline.co:8080/item?id=...". The three id's were 0,1, and 2. After messing with the id, I found when I passed in a single quote (') that I get an internal server error; however, when I passed in a double quote (") the website worked fine. This told me that the database query is of this format "SELECT * FROM pages WHERE id=''". After several minutes and several attempts of changing the query I found 'or '1'='1 gave me what I wanted. The needed url looks like this "http://cornerstoneairlines.co:8080/item?id=1' or '1'='1". The page that renders featured a table, with the above flag found inside it.*


### Part 2 (30 Pts)
*Question 1 : For the first question I inputed a script tag with an alert() function found inside to get me to the next questions. 
"<scipt> alert(); </script>"*

*Question 2 : For this question I thought the script tag would work once again; however my thought process was wrong. It took me several minutes and a hint to figure out that I needed to pass in an img that does not exist in order to get a "onerror", which generates a alert.*

*Question 3 : For this question I needed all three hints. After rereading the hints over and over I found that this was a Dom-based injection. I entered in the following address https://xss-game.appspot.com/level3/frame#default= to get the alert to pop up.*

*Question 4 : For this question I used all three hints again, and viewed the source code. After several minutes of looking at the source code I noticed that when the timer is started, it is using the users input. So, by using this input 1}}'); alert('{{ I was able to get the alert to pop up. This allows the timer to start, end and then call the alert function.*

*Question 5 : This question took me a while to figure out. I viewed all the pages several times, until i realized that I could enter a value for next on the signup page. Looking at the source code I found <a href="{{ next }}">Next >></a>, {{ next }} is also found on the confirm page after signing up. So instead of having the signup page show confirm I pass ing javascript:alert() to get the alert to pop up. https://xss-game.appspot.com/level5/frame/signup?next=javascript:alert()*

*Question 6 : For this question I also use all the hints and view the page source. I see that the javascript file is uploaded via the DOM. The security check only checks for the string http in the javascript file. The hints told me that GOOGLE provides an API which I can use to trigger the alert I need. Since the security check is case sensitive I pass the GOOGLE API link to the jsapi file to get the alert to pop up.  https://xss-game.appspot.com/level6/frame#HTTPs://www.google.com/jsapi?callback=alert*