#request and sys are two packages. Had to install requests using pip at first run.
import requests
import sys
import json
from pprint import pprint

#two variables to squeeze a string between these two so it will become a full uri
part1 = 'https://api.companieshouse.gov.uk/company/'
part2 = '/persons-with-significant-control'
part3 = '/'
#open the outputfile before the for loop
text_file = open("uri.txt", "w")


#open a new file textfile for saving the responses from the api
text_file = open("responses.txt", "w")

#send every uri to the api, with authentification code and write the respsones to a textfile
with open('CHcodes.txt', 'r') as f2:
   for i in f2:
         uri = part1 + i.strip(' \n\t') + part2
         uri3 = part1 + i.strip(' \n\t') + part3
         pscquery = requests.get(uri, auth=('eXzVc8YCQTurqUFruK76WZ9cGsYwpWbeNVTiIaMt', ''))
         compquery = requests.get(uri3, auth=('eXzVc8YCQTurqUFruK76WZ9cGsYwpWbeNVTiIaMt', ''))
         pscinfo = pscquery.text
         compinfo = compquery.text
         print(i)
         print(pscinfo)
         print(compinfo)
         comp_file = open("comp.json", "w")
         comp_file.write(compinfo)
         comp_file.close()
         with open('comp.json') as json_data:
            compdata = json.load(json_data)
            text_file.write(compdata['company_name'])
            text_file.write("\n")
            text_file.write(i)
            text_file.write("date of creation: ")
            text_file.write(compdata['date_of_creation'])
            text_file.write("\n")
            text_file.write(uri)
            text_file.write('\n')
            text_file.write(pscinfo)
            text_file.write('\n')
            text_file.write('\n')   
            text_file.write('\n') 
text_file.close()

text_file.close()
text_file.close()