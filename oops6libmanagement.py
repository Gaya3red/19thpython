class Library:
    book = ["The fault in our stars","Alang","Citadel"]
    author_book = {
        "Pablo":["escobar","escobar returns","escobar part3"]
    }
    def getallBooks():
        pass
    def addBook():
        pass
    def getBookByAuthorName(authorName):
        for key in author_book:
            if key == authorName:
                print(author_book[key])
        pass
    def sortBooksInTopologicalOrder():
        pass
    def getAllSubscribers():
        pass
    def getUnavailableBooks():
        pass
    def mapAuthorWithaBook():
        pass
class MyLibrary(Library):
    def getFaviourBook():
        pass
    def getFaviourCustomer():
#code incomplete
