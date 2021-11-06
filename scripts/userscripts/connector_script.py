import pywikibot
enwiki = pywikibot.Site('en', 'wikipedia')
enwiki_repo = enwiki.data_repository()
from collections import defaultdict
import operator

def getPageData(pagename):
    return pywikibot.Page(enwiki_repo, pagename)

def editWikiPage(page_data, new_text):

    page_text = page_data.get() 
    page_data.text = page_text + "\n"*2 + new_text

    try:    
        page_data.save("Done updating")
    except:
        print(page_data.text)
        print("Did not work")

print("Updating the wiki page")   
page_name = 'User:Kelvin_Wachira/Outreachy_1'
editWikiPage(getPageData(page_name), "Hello")
print("*-*"*10)

site = pywikibot.Site('en', 'wikipedia')  # any site will work, this is just an example
repo = site.data_repository()  # this is a DataSite object

def extractWikidataItemInfor(item):
    item.get()
    if 'en' in item.labels: # check if item has label in english 
        print('The item {}, wiki Article label in English is: {}'.format( item.title, item.labels['en']))
    
    if item.claims:
        if "P31" in item.claims: # meaning there is an instance of Statements
            child_item_label = item.claims['P31'][0].getTarget().labels
            if child_item_label: print("It is an instance of {}".format(child_item_label['en']))
        else: print("Item does not have an instance statement")

        for P in item.claims.keys(): #populate the property_occurence dictionary
            property_occurence[P] +=1


    print("*"*10)
    return 0

first_task_items = [ "Q7725634", "Q216353", "Q24925", 
"Q277759", "Q6581097" , "Q48264" ,"Q508553", "Q34647",
"Q534643", "Q1377772" ]

property_occurence = defaultdict(int) # stores the number occurence of properties in the listed items
for  Qnumber in first_task_items:
    item = pywikibot.ItemPage(repo, Qnumber)
    extractWikidataItemInfor(item)

max_P_occurence = max(property_occurence.items(), key=operator.itemgetter(1))[0] #get which property occured the most

print("The property that occurs the most times in the listed items is : {}".format(max_P_occurence))







  # This will be functionally the 
# item.get()  # you need to call it to access any data.]
# print(type(item))
# print(item.title())
# sitelinks = item.sitelinks  # a map of links in site
# aliases = item.aliases  # other names of that item in other languages
# itemlabels = item.labels
# itemclaims = item.claims

# c = 0
# for k, v in itemclaims.items():
#     c+=1