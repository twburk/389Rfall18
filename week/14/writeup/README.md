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
