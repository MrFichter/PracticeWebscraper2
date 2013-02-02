
import re


content = '<<h3 class="field-content"><a href="/node/33583">Public Computer Service Restored</a></h3>'
  

headerForScrub = re.findall ('\d">.*</a' , content)

stringHeader = str(headerForScrub)

frontScrub = re.sub('\d">' , '' , stringHeader )
backScrub = re.sub ('</a' , '' , frontScrub)


print 'HEADER:' , backScrub
            

##separateLines = re.split ('\n+' , content)

##for i in range (len(separateLines)):
##    desiredResults = re.findall('(?i).*book.*', separateLines[i])
##    if len (desiredResults) > 0:
##        print 'HEADER' , separateLines[i-3]
##        print '\n'
##        print 'CONTENT' , desiredResults
##
##

        




