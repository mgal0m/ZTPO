import httplib2
from bs4 import BeautifulSoup
import re

class GetUserId():
    basicUrl = "https://suw.biblos.pk.edu.pl/browseByAuthor&letter="
    name = ""
    surname = ""
    firstLetter = ""
    source = ""

    def addSurname(self, surname, name):
        self.surname = surname
        self.name = name
        self.firstLetter = surname[0]

    def getSource(self):
        http = httplib2.Http()
        status, response = http.request(self.basicUrl+self.firstLetter)
        soup = BeautifulSoup(response, 'html.parser')
        self.source = soup

    def findIdBySurname(self):
        href = re.compile('^userHomepage&uId')
        idUrl = ""
        for a in self.source.find_all('a', href=href):
            text = str(a.contents)
            text = text[0:30]
            if self.surname in text and self.name in text:
                idUrl = a['href']
                x = re.compile('\d+')
                x = re.findall(x, idUrl)
                return x[0]
                break

    def getId(self, surname, name):
        self.addSurname(surname, name)
        self.getSource()
        id = self.findIdBySurname()
        return id
        
          
