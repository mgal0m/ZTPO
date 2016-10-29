from GetUserId import *
from GetNumberOfPublications import *
from GetUserPublications import *
from unidecode import unidecode


if __name__ == "__main__":
    x = GetUserId()
    id = x.getId("Kantor", "Ryszard")
    print(id)
    z = GetNumberOfPublications()
    pagenum = z.getNumberOfPublications(id)
    print(pagenum)
    c = GetUserPublications()
    title, typeName, form, date, mnsiwPoints = c.getAllPublications(id, pagenum)
    #print(title)
    #print(typeName)
    #print(form)
    #print(date)
    #print(mnsiwPoints)
    print(len(title))
    for i in title:
        print(i)