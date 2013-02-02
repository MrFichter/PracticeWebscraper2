
import re


content = '''
 <div class="views-field views-field-title">        <h3 class="field-content"><a href="/node/33583">Public Computer Service Restored</a></h3>  </div>  
  <div class="views-field views-field-field-subtitle">        <h4 class="field-content"></h4>  </div>  
  <div class="views-field views-field-created">        <h5 class="field-content">Published on Friday, January 11, 2013</h5>  </div>  
  <div class="views-field views-field-body">        <div class="field-content"><p> Access to public computers has been restored at DC Public Library locations.<br /><br />Express computers continue to be available, as well as other options for information access: WiFi is available, and you can access your account via our <a href="http://dclibrary.org/appstore" title="DC Public Library mobile apps">mobile apps</a>. As always, our library staff are happy to help you with any questions you have.<br /><br />Thank you for your continued patience. <br /></p>
</div>  </div>  
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/33583">Read full article</a></span>  </div>  </div>
  <div class="views-row views-row-4 views-row-even">

 <div class="views-field views-field-title">        <h3 class="field-content"><a href="/node/33175">DC Public Library Collects Toys and Books for Children With HIV/AIDS</a></h3>  </div>  
  <div class="views-field views-field-field-subtitle">        <h4 class="field-content"></h4>  </div>  
  <div class="views-field views-field-created">        <h5 class="field-content">Published on Monday, December 10, 2012</h5>  </div>  
  <div class="views-field views-field-body">        <div class="field-content"><p> The DC Public Library, in partnership with Bread for the Soul, will collect new, unwrapped toys and books for children with HIV/AIDS and children whose parents have the disease.  <br /><br />The toy drive runs through December 14 for children one – 12 years old. Toys and books can be dropped off at any of the 25 public libraries across the District.  Also partnering with the DC Public Library and Bread for the Soul are  DC Water and the Department of Public Works. <br /><br />Bread for the Soul is a community organization that works with families living with HIV/Aids.  For more information and a list of library locations, visit the DC Public Library at dclibrary.org or call 727-1222. </p>
</div>  </div>  
  <div class="views-field views-field-view-node">        <span class="field-content"><a href="/node/33175">Read full article</a></span>  </div>  </div>
  <div class="views-row views-row-8 views-row-even">

  '''






header = '((?i)<h3 class="field-content"><a href="/node/.*)'

desiredResults = re.search('((?i)<h3 class="field-content"><a href="/node/.*)' '(.*)' '(book)', content)

##print desiredResults   
groupedResults = desiredResults.group(1,3)
print groupedResults

   
