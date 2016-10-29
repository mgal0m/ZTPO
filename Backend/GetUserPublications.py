from bs4 import BeautifulSoup
from selenium import webdriver
import re
from const import *

class GetUserPublications():
    basicUrl3 = "&rsAt="
    source = ""
    userId = ""
    numbersOfPublications = 0
    page = 0

    def addId(self, userId):
        self.userId = userId

    def addNumbersOfPublications(self, numbersOfPublications):
        self.numbersOfPublications = int(numbersOfPublications)

    def addPageNumbers(self, pageNumbers):
        self.pageNumbers = pageNumbers

    def getSource(self, page):
        wd = webdriver.Chrome('libs/chromedriver.exe') #later switch to phantomjs
        wd.get(BASE_URL+PUB_NUM_URL+str(self.userId)+"&rel=BPP-author")
        wd.get(BASE_URL+PUBLICATIONS_URL+str(self.userId)+"&rsAt="+str(self.page))
        self.source = BeautifulSoup(wd.page_source, 'html.parser')

    def getPublications(self):
        text = self.source.find_all(text=True)
        typeIndex = []
        title = []
        typeName = []
        mniswPoints = []
        for i, j in enumerate(text):
            if j==' Punktacja czasopisma na Liście MNiSW: ':
                typeIndex.append(i) # do wyjebania?
                mniswPoints.append(text[i+1])
                title.append(text[i-7])
                typeName.append(text[i-5])
        return title, typeName, mniswPoints

    def getAllPublications(self, userId, numbersOfPublications):
        self.addId(userId)
        self.addNumbersOfPublications(numbersOfPublications)
        if self.numbersOfPublications <= 20:
            self.page = 0
            self.getSource(self.page)
            title, typeName, mniswPoints = self.getPublications()
            return title, typeName, mniswPoints
        elif self.numbersOfPublications > 21:
            self.page = 0
            self.getSource(self.page)
            title, typeName, mniswPoints = self.getAllPublications()
            pages = self.numbersOfPublications/20
            int(pages)
            while pages!=1:
                self.page += 20
                self.getSource(self.page)
                title1, typeName1, mniswPoints1 = self.getAllPublications()
                title += title1
                typeName += typeName1
                mniswPoints += mniswPoints1
                pages-=1
            return title, typeName, mniswPoints



       

"""
if __name__ == "__main__":
    x = GetUserPublications()
    x.addId(3322)
    x.getSource()
    print("click any key than enter")
    d = input()
    a, b, c = x.getPublications()
    print(a)
    print(b)
    print(c)
"""



    
        
          
