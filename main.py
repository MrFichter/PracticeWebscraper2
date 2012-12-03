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


SEARCHTERMS = ('technology' , 'tech ' , 'student' , 'students' ,
               'hackathon' , 'hack' , 'hacker' , 'hackers' , 'mobile' ,
               'computer' , 'computers' )


import urllib2 ## There's also urllib, but @Fichtitious recommended urllib2.

page = urllib2.urlopen ('http://www.dclibrary.org/newsreleases')

content = page.read() ## Some people on the #python freenode irc recommended this.


##@Fichtitious recommended the below for my
##PracticeWebscraper, but I'm not sure if it
##will work with the current project.
##import json
##forecast = json.load (page)


###Next step: Learn some string parsing
##so that I can make sense of all of the
##information that gets returned when
##I execute page.read().
##@Fichtitious recommended dots and stars.



##Moved folder from my desktop.

'''
<h3 class="field-content"><a href="/node/29718">Photo/Film Requests</a></h3>

<h3 class="field-content"><a href="/node/31486">Chris Tonjes Appointed Chief Information Officer of Baltimore, MD </a></h3>  </div>  

'''
