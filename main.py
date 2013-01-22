##The purpose of this program is to open
##the url below and search the content
##for the desired terms in my SearchTerms
##tuple.If I can figure out how to return 
##some context surrounding the search 
##terms,like the paragraph they are in 
##or the heading under which they appear,
##that would be great.
##
##The main purpose of creating this 
##program is to help me learn how to do 
##basic webscraping. 
##
##Another important goal is to respect all 
##legal and ethical guidelines related to 
##webscraping, so please let me know if I 
##have overlooked any of these.
##
##This project is a sequel to my 
##PracticeWebscraper project, which
##was easier because it accessed an
##API that organized its data into a
##neat set of nested dictionaries.
##https://github.com/MrFichter/PracticeWebscraper/blob/master/PracticeWebscraper.py



SEARCHTERMS = ('technology' , 'tech ' , 'student' , 'hackathon' , 'hack' , 'hacker' , 'hackers' , 'mobile' ,
               'computer' , 'book' ) ### book is for testing purposes. 
##Learning note: Searching for 'book' appears to find 'books' without
##a problem.


results = []


import urllib2 ## There's also urllib, but @Fichtitious \
##recommended urllib2.

page = urllib2.urlopen ('http://www.dclibrary.org/newsreleases')

content = page.read() 


import re


for term in SEARCHTERMS:

    body = re.compile('(?i)<p>(.*)' + term + '(.*)</p>')

##re.findall () returns results at a list.
    bodyResults = re.findall (body, content)


    
###If the next few lines worked, it would search for just the headers \
###followed by successful search term hits.
##    if len (bodyResults) > 0:
##        for i in bodyResults:
##            header = re.compile ('<h3 class="field-content"><a href="/node/(.*)>(.*)' + bodyResults[i])
##        
###I still need a way to find just the headers associated with search terms.
##
##    header = re.compile ('<h3 class="field-content"><a href="/node/(.*)>(.*)</a></h3>')
##    headerResults = re.findall(header, content)
    
    
    
    termUpper = [str.upper (term)] #A label to help separate term results.
##It might print funny with listPrintLineBreaks, but I don't care.

    results.append (termUpper)
##    results.append (headerResults)
    results.append (bodyResults)


    
from listPrintLineBreaks import listPrintLineBreaks
listPrintLineBreaks (results)




##-----------------------------
##Next step: Right now, the program returns the search
##term and a few words next to it from one re.findall() and the headlines,
##plus some another garbage, as the results of another re.findall(). It
##would be more useful if I could do the following:
##1) Find the only headline corresponding to the news item in which the
##search term appears.
##2) Find the publication date. (The tip from @Fichtitious
##should help a lot here.)
##3) Find a few more context words surrounding the search term.
##Maybe get the whole sentence. That would be cool.
##4) Store all of the above into a dictionary.
##5) Maybe prompt the user (me, I'm assuming) to enter a
##numerical rating of how interesting or relevant the article
##was. Save the rating in the dictionary.

##Eventual step: apply some of the more advanced
##moves @Fichtitious mentioned in the email he sent me.


##Things that might help me with next step #1:
##For #1, here are two examples of what headlines
##look like:
##<h3 class="field-content"><a href="/node/29718">Photo/Film Requests</a></h3>
##<h3 class="field-content"><a href="/node/31486">Chris Tonjes Appointed Chief Information Officer of Baltimore, MD </a></h3>  </div>  
##Also, @Fichtitious gave me this link to help me see more
##terms I can use with re:
##http://docs.python.org/2/library/re.html
##One of the examples @Fichtitious emailed me shows
##how to tell the program to stop returning something when it hits
##an html tag like </h3>. So, if I can figure out
##how to use a found instance of a search term as a
##starting point and then backtrack to a tag starting with
##<h3, I might be onto something. I could find
##where on the page the word 'technology' gets mentioned,
##for instance, then leap back a bit and find the headline
##of that article!







