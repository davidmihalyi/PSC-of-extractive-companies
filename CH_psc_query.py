#request and sys are two packages. Had to install requests using pip at first run.
import requests
import sys
import json
from pprint import pprint

#two variables to squeeze a string between these two so it will become a full uri
part1 = 'https://api.companieshouse.gov.uk/company/'
part2 = '/persons-with-significant-control'
part3 = '/'


#open a new file textfile for saving the responses from the api
text_file = open("PSC_detail.txt", "w")
text_file.write("CH id, PSC 1, country 1, control 1, PSC2, country 2, control 2")
text_file.write('\n') 

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
         psc_file = open("psc.json", "w")
         psc_file.write(pscinfo)
         psc_file.close()

         with open('psc.json') as json_data:
            pscdata = json.load(json_data)
            text_file.write(i.strip(' \n\t'))
            text_file.write(", ")
            if 'items' in pscdata:
                  text_file.write(pscdata['items'][0]['name'])
                  text_file.write(", ")
                  if 'country_registered' in pscdata['items'][0]['identification']:
                        text_file.write(pscdata['items'][0]['identification']['country_registered'])
                  text_file.write(", ")
                  text_file.write(pscdata['items'][0]['natures_of_control'][0])
                  text_file.write(", ")
                  if pscdata['total_results']==2:
                     text_file.write(pscdata['items'][1]['name'])
                     text_file.write(", ")
                     if 'country_registered' in pscdata['items'][1]['identification']:
                        text_file.write(pscdata['items'][1]['identification']['country_registered'])   
                     text_file.write(", ")
                     text_file.write(pscdata['items'][1]['natures_of_control'][0])
                     text_file.write(", ")
            else:
                  text_file.write("no PSC")
            text_file.write('\n')
 
text_file.close()
