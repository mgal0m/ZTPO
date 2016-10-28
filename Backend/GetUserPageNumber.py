import httplib2
from bs4 import BeautifulSoup
import re
from const import *

class GetUserPageNumber():
    userId = ""
    source = ""

    def addId(self, userId):
        self.userId = userId

    def getSource(self):
        http = httplib2.Http()
        status, response = http.request(BASE_URL+PUB_NUM_URL+self.userId)
        soup = BeautifulSoup(response, 'html.parser')
        self.source = soup

    def getPageNumbers(self):
        text = str(self.source.find_all('h4'))
        x = re.compile('\d+')
        pageNumbers = re.findall(x, text)
        return pageNumbers[1]
        
          
