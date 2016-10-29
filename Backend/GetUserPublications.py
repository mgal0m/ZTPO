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
        self.source = BeautifulSoup(wd.page_source, 'html.parser')


    def getPublications(self):
        text = self.source.find_all(text=True)
        typeIndex = []
        title = []
        typeName = []
        for i, j in enumerate(text):
            if j==' typ: ':
                typeIndex.append(i)
                title.append(text[i-1])
                typeName.append(text[i+1])
        return title, typeName
       


if __name__ == "__main__":
    x = GetUserPublications()
    x.addId(3322)
    x.getSource()
    print("click any key than enter")
    d = input()
    a, b = x.getPublications()
    print(a)
    print(b)


"""
x = soup.find_all(text=True)
for i, j in enumerate(x):
	if j==' Punktacja czasopisma na Liście MNiSW: ':
		print(i)

   """ 


    
        
          
