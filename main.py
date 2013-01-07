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
               'computer' , 'book' ) ### book is for testing purposes
##Learning note: Searching for 'book' appears to find 'books' without
##a problem.

results = []
printableResults = [] ## This list will include labels \
##indicating to which search term the results correspond.

import urllib2 ## There's also urllib, but @Fichtitious \
##recommended urllib2.

page = urllib2.urlopen ('http://www.dclibrary.org/newsreleases')

content = page.read() ## Some people on the #python freenode irc \
##recommended this.

import re
for term in SEARCHTERMS:
    termResults = re.findall ('(?i)' + term + '.*' , content) ## '(?i)' \
##makes it case insensitive. It needs to come at the beginning, though.
## I learned about using '(?i)' or other (?iLmsux) terms from here:
##http://stackoverflow.com/questions/500864/case-insensitive-python-regular-expression-without-re-compile
##(See answer from aem999.)
##Aem999 uses and r before the expression, which treats the string a a raw
##string and would ignore the symbolism of things like \n, as explained here:
##http://stackoverflow.com/questions/4780088/in-python-what-does-preceding-a-string-literal-with-r-mean
##Note: <bob_f> from the python irc recommended an altnerative strategy:
##MrFichter: Yes, create your regex using \
##re.compile and pass flags=re.IGNORECASE
## See @Roger Pate's comments about re.compile here: http://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile

##The line above is inspired by a line @Fichtitious
##mentioned in a tutorial email he sent me:
##re.findall('Published on.*', content)
##@Fichtitious explained the following:
##''.' is the wildcard character, and '*' means 0 or
##more occurrences of the preceding character.  So
##'.*' means go match 0 or more of anything, and
##'Published on.*' means go match 'Published on'
##followed by 0 or more of anything.
##By default, all re matches go only as far as
##the end of the line, so this time we matched each
##occurrence of 'Published on' and all the
##characters coming after it until the next newline.'
##I wasn't sure if I'd be able to concatenate
##'.*' with my variable 'term,' but it looks like
##this worked!

##re.findall () returns results at a list

    results.append (termResults)

    termLabel = ['RESULTS FOR TERM: ' + str.upper (term)]
    printableResults.append (termLabel)
    printableResults.append (termResults)

from listPrintLineBreaks import listPrintLineBreaks
listPrintLineBreaks (printableResults)



##-----------------------------
##Next step: Right now, the program returns the search
##term and a few words next to it. It would be more useful
##if I could do the following:
## (3/4) Find a good way to archive old commentary. Maybe
## make them a separate text document.
##1) Find the headline of the news item in which the search
##term appears.
##2) Find the publication date. (The tip from @Fichtitious
##should help a lot here.)
##3) Find a few more context words surrounding the search term.
##Maybe get the whole sentence. That would be cool.
##4) Store all of the above into a dictionary.
##5) Maybe prompt the user (me, I'm assuming) to enter a
##numerical rating of how interesting or relevant the article
##was. Save the rating in the dictionary.


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


###Eventual step: apply some of the more advanced
###moves @Fichtitious mentioned in the email he sent me.


##----------------------------------
##OUTTAKE
##@Fichtitious recommended the below for my
##PracticeWebscraper project, but I'm not sure if it
##will work with the current project.
##import json
##forecast = json.load (page)



