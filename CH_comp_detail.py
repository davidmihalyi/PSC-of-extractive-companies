#request and sys are two packages. Had to install requests using pip at first run.
import requests
import sys
import json
from pprint import pprint

#two variables to squeeze a string between these two so it will become a full uri
part1 = 'https://api.companieshouse.gov.uk/company/'
part2 = '/'


comp_detail = open("comp_detail.txt", "w")
comp_detail.write("company name, CH id, status, type, date of creation, postcode, jurisdiction")
comp_detail.write('\n') 

with open('CHcodes.txt', 'r') as f2:
   for i in f2:
         uri = part1 + i.strip(' \n\t') + part2
         compquery = requests.get(uri, auth=('eXzVc8YCQTurqUFruK76WZ9cGsYwpWbeNVTiIaMt', ''))
         compinfo = compquery.text
         print(i)
         comp_file = open("comp.json", "w")
         comp_file.write(compinfo)
         comp_file.close()
         with open('comp.json') as json_data:
            compdata = json.load(json_data)
            comp_detail.write(compdata['company_name'])
            comp_detail.write(", ")
            comp_detail.write(i.strip(' \n\t'))
            comp_detail.write(", ")
            comp_detail.write(compdata['company_status'])
            comp_detail.write(", ")
            comp_detail.write(compdata['type'])
            comp_detail.write(", ")
            comp_detail.write(compdata['date_of_creation'])
            comp_detail.write(", ")
            comp_detail.write(compdata['registered_office_address']['postal_code'])
            comp_detail.write(", ")
            comp_detail.write(compdata['jurisdiction'])
            comp_detail.write(", ")
            comp_detail.write('\n') 
         
comp_detail.close()
