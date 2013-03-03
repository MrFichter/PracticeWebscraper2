import urllib2 ## There's also urllib, but @Fichtitious \
##recommended urllib2.


rawPage = urllib2.urlopen ('http://www.dclibrary.org/newsreleases')
rawContent = rawPage.read()


import re



##LOOKAHEAD STRATEGY

results = re.findall ('<h3 (?=weather)', rawContent)





'''
##NEW LINES AT PARAGRAPH BREAKS STRATEGY

headerNonGreedy = '<h3 class.*?h3'
headerGreedy = '<h3 class.*h3' ## Yields same results as headerNonGreedy.
anythingNonGreedy = '.*?' ## Doesn't seem to do much.
term = 'weather'
endParagraph = '</a></span>  </div>  </div>'



pageWithoutNewLines = re.sub ('\n' , '' , rawContent) ## Remove all new-\
##line characters.


pageWithParagraphBreaks = re.sub (endParagraph , '\n' , pageWithoutNewLines)
##puts line breaks at the ends of paragraphs





results = re.findall (headerGreedy + '.*' + term + '.*' + '\n', \
pageWithParagraphBreaks) ##Putting the \ character above does not seem \
##to cause any problems.

'''


