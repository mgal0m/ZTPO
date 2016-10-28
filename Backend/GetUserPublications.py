import httplib2
from bs4 import BeautifulSoup
from selenium import webdriver
import re
from const import *

class GetUserPublications():
    basicUrl3 = "&rsAt="
    source = ""
    userId = ""

    def addId(self, userId):
        self.userId = userId

    def getSource(self):
        wd = webdriver.Chrome('libs/chromedriver.exe') #later switch to phantomjs
        wd.get(BASE_URL+PUB_NUM_URL+str(self.userId)+"&rel=BPP-author")
        wd.get(BASE_URL+PUBLICATIONS_URL+str(self.userId)+"&rsAt="+"0")
        self.source = wd.page_source

if __name__ == "__main__":
    x = GetUserPublications()
    x.addId(3322)
    x.getSource()
    print("click any key than enter")
    d = input()
    print(x.source)

    


    
        
          
