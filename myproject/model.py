from myproject import model_Fun
import os


class WedCreator():

    def __init__(self, JSON_path):
        self.file = model_Fun.readJSON(JSON_path)
        self.path = os.path.join(JSON_path)
        self.reqvalueFromURL()

    def printInfo(self):
        print(self.file["info"])

    def printWorkPath(self):
        print(os.getcwd())

    def reqvalueFromURL(self,  status_output=False):
        # try:

        def __keyExistDict(dictionary, key):
            return dictionary[key] if (key in dictionary) else None

        if status_output:
            print("Info：")
            print(self.file["info"])

        wed = model_Fun.reqURL(self.file["info"]["URL"])

        HTMLcode = []
        HTMLcode.append(wed)
        for method in self.file["method"]:
            HTMLcode = model_Fun.analysis(
                HTMLcode,
                __keyExistDict(method, "HTMLtag"),
                __keyExistDict(method, "searchTag"),
                __keyExistDict(method, "searchString"),
                __keyExistDict(method, "onlyChildren")
            )
            if status_output:
                print("完成執行參數：")
                print(method)

        if status_output:
            print("執行結束，輸出數值：")
            print(HTMLcode)

        self.value = HTMLcode
        self.css = model_Fun.css_analysis(self.file["info"]["URL"], wed)

        # except BaseException as err:
        #     print(err)

    def writeJSON(self, path):
        model_Fun.writeJSON(path, self.value)


if __name__ == "__main__":

    # URI = 'http://www.tcivs.tc.edu.tw/ischool/publish_page/122/?cid=6119'
    # print(model_Fun.request(URI).text)

    path = ("web/網頁調適/Server Side/Crawler/demo1.json")
    # reqvalueFromURL(self.path)
    # self.path = ("web/網頁調適/Server Side/Crawler/demo2.json")
    # reqvalueFromURL(self.path, 1)

    english = WedCreator(path)
    # english.printWorkPath()
    # english.printInfo()

    english.reqvalueFromURL()
    print(english.value)
    english.writeJSON(os.getcwd())
    # english.writeJSON(english.path)
    # english.print_info()
    # english.reqvalueFromURL(True)
