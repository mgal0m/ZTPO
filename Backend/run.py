from GetUserId import *
from GetUserPageNumber import *

if __name__ == "__main__":
    x = GetUserId()
    id = x.getId("Góra", "Marta")
    print(id)
    z = GetUserPageNumber()
    pagenum = z.getPageNumbers(id)
    print(pagenum)