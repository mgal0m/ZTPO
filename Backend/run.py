from GetUserId import *
from GetNumberOfPublications import *
from GetUserPublications import *

if __name__ == "__main__":
    x = GetUserId()
    id = x.getId("Góra", "Marta")
    print(id)
    z = GetNumberOfPublications()
    pagenum = z.getNumberOfPublications(id)
    print(pagenum)
    c = GetUserPublications()
    title, typeName, form, date, mnsiwPoints = c.getAllPublications(id, pagenum)
    print(title)
    print(typeName)
    print(form)
    print(date)
    print(mnsiwPoints)