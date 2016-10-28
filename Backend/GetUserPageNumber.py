import httplib2
from bs4 import BeautifulSoup
import re

class GetUserPageNumber():
    basicUrl = "http://suw.biblos.pk.edu.pl/userHomepage&uId="
    basicUrl2 = "&rel=BPP-author"
    userId = ""
    source = ""

    def addId(self, userId):
        self.userId = userId

    def getSource(self):
        http = httplib2.Http()
        status, response = http.request(self.basicUrl+self.userId+
                                        self.basicUrl2)
        soup = BeautifulSoup(response, 'html.parser')
        self.source = soup

    def getPageNumbers(self):
        text = str(self.source.find_all('h4'))
        x = re.compile('\d+')
        pageNumbers = re.findall(x, text)
        return pageNumbers[1]
        
          
