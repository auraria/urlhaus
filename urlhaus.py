from bs4 import BeautifulSoup
import requests
import json
import re
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


urls = [] #list of urlhaus urls used to search domains
lookup = [] #list of lookup responses

class urlhaus:
    def __init__(self, argv): ##init which assigned the output from req to ip
        self.ip = argv #take value of ip which is input from req and assigns it to self.ip
        for i in self.ip: #loop to pull ip arguments
            self.url = 'https://urlhaus.abuse.ch/browse.php?search={}'.format(i) #urlhaus url to search with the ip from self.ip in the url to search
            urls.append(self.url) #appends robtex url with ips to search to the urls list
       

    def get(self):
        for u in urls: #loop to go through urls in the urls list
            response = requests.get(u, verify=False) #get request to completed robtex url from above
            soup = BeautifulSoup(response.text, 'html.parser')  #use Beautifulsoup's html parser for the output and assign that to soup
            #results = soup.find_all('div', class_='dns')    #take html output from soup, find all div sets, under the class dns(this is all found from the html output itself)
            results2 = re.findall(r"(?<=\>)http.*(?=\<\/a\>\<\/td\>\<td\>\<span class\=\"badge badge-danger\"\>)", str(soup), re.M|re.I) #regex find all non-html data we want to view
            #+print(str(soup))
            print(str(results2))

            

            
req = urlhaus(sys.argv[1:]) #allows the use of arguments in urlhaus script
#req = robtex(input('Place your ip address here: ')) #take user input and assign it to robtex class which is passed to arg ip
req.get() #runs get function with req assigned arg

for l in lookup: #looping through the lookup array
    print(l) #print individual lookups