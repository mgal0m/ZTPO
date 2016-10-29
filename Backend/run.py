from GetUserId import *
from GetNumberOfPublications import *
from GetUserPublications import *

if __name__ == "__main__":
    x = GetUserId()
    id = x.getId("Anielak", "Anna")
    print(id)
    z = GetNumberOfPublications()
    pagenum = z.getNumberOfPublications(id)
    print(pagenum)
    c = GetUserPublications()
    title, typeName, mnsiwPoints = c.getAllPublications(id, pagenum)
    print(title)
    print(typeName)
    print(mnsiwPoints)