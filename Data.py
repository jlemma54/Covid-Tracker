from WebScraper import WebScraper

class Data:


    information = WebScraper()
    data = information.getInfo()

    def printOutInfo(self):
        return Data.data


a = Data().printOutInfo()
print(a)