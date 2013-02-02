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
               'computer')  
##Learning note: Searching for a singular appears to find the plural without
##a problem.


results = []


import urllib2 ## There's also urllib, but @Fichtitious \
##recommended urllib2.

page = urllib2.urlopen ('http://www.dclibrary.org/newsreleases')

content = page.read() 

import re



separateLines = re.split ('\n+' , content)
##Got re.split idea from:
##http://docs.python.org/2/library/re.html#making-a-phonebook
###Would it be easier to write it to a file and just go line by line through \
###the file?





for i in range (len(separateLines)):

    for term in SEARCHTERMS:

        termResults = re.findall('(?i).*' + term + '.*', separateLines[i])

        if len (termResults) > 0: ## i.e If it's a real hit....

            header = '\d">.*</a' ##From the HTML. \d means one digit.
            strHeader = str(re.findall(header, separateLines[i-3])) ## Why \
##            i-3? Because the header comes three lines before the content
##            in this document.
            ###Could I skip the i-3 if I knew how to do backreferencing or
            ###multiline searches?
            frontHeaderScrub = re.sub('\d">' , '' , strHeader ) ##Replaces \
##            the HTML in front with nothing
            allHeaderScrub = re.sub ('</a' , '' , frontHeaderScrub) ##Scrubs \
##            back, too.
           

            termUpper = [str.upper (term)] #A label to help separate term results.

##            results.append (termUpper)
##            results.append (allHeaderScrub)

            print '\n'
            print ' TERM:' , termUpper
            print 'HEADER:' , allHeaderScrub
            print 'CONTENT:' , termResults
            print '\n'
                



    

    
##from listPrintLineBreaks import listPrintLineBreaks
##listPrintLineBreaks (results)


