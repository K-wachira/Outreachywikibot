import pywikibot
import requests

enwiki = pywikibot.Site('en', 'wikipedia')
endpoint = "https://www.wikidata.org/w/api.php"
en_repo = enwiki.data_repository()

def isEqual(search_results_text, search_request_text):
  return search_results_text.lower() == search_request_text.lower()


# Printing the search results from the itemfinder function 
def printComponents(search_obj, search_term):
  print(search_obj)
  return
  for item in search_obj['search']:
    if isEqual(item['match']['text'], search_term ):
      print("The Quip search of {} has an id of {} and it is a Positive match  and can be found on this {} url".format(search_term, item['title'], item['url'][2:]  ))
    else:
      print("The Quip search of {} has an id of {} and it is a False Positive match and can be found on this {} url".format(search_term, item['title'], item['url'][2:]  ))

# Function that searches for the quip on wiki data.
def itemFinder(item,limit): 
    parameters = {
    'action': 'wbsearchentities',
    'search': item,
    'language': 'en',
    'limit': limit,
    'format': 'json'
    }
    response = responseHelper(parameters)
    printComponents(response, item)
    print("*"*100, "\n"*3)

    
def responseHelper(parameters):
  return requests.get(endpoint, params=parameters).json()

# Uncategorized items
def uncategorizedItemFinder(item, limit):
    params ={
    "qplimit": limit,
    "action": "query",
    "": "Uncategorizedpages",
    "list": "querypage",
    "format": "json"
    }
    response = responseHelper(params)
    for bucket in response['query']['querypage']['results']:
        if item in bucket['title']:  print("Searched item(" +item+") was found in the uncategorized page's title ")


# This function helps in validating the limit the user puts as input
def searchResultsLimit():
  print('how many search results do you want (Must be a number greater than 0):')
  limit = int(input())
  while limit <= 0:
      print('Error, Please enter a number that is greater than 0:')
      limit = int(input())
  return limit







# This function serves as the initializer to the script and helps in getting user input
def main():
  print("Welcome to Wikimedia search script. \nWhat would you like to do?")
  print("""
          1: Custom search. \n
          2. Default search. \n
          Any other characters to exit \n(1 or 2): """)
  userinput = input()
  if userinput == "1":
    print("You chose Custom search. Please enter different strings what you want to search separated by a comma ','")
    userinput2 = input()
    userinput2 = userinput2.split(',')
  elif userinput == "2":
      print("You chose Default search.")
      userinput2 =  ["abc", "movies", "series"]
  else: exit()
  limit = searchResultsLimit()

  print("Categorized "+ "*" * 10 )
  for item in userinput2:
      itemFinder(item,limit)
  print("Uncategorized "+ "*" * 10 )

  for item in userinput2:
    uncategorizedItemFinder(item,limit)
main()


