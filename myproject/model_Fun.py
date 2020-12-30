import requests
from bs4 import BeautifulSoup

from urllib.parse import urljoin
from urllib.parse import urlparse

import json
import os
import re


# class FileTool():
#     def __init__(self, __file_path):
#         self.__file_path = __file_path

#     def readJSON(self):
#         try:
#             with open(self.__file_path, mode='r', encoding='utf-8') as JSON_file:
#                 return json.load(JSON_file)

#         except BaseException as err:
#             print(err)
#             print(os.getcwd())  # 顯示路徑

#     def writeJSON(path, write):
#         try:
#             with open(path, mode='w', encoding='utf-8') as JSON_file:
#                 for i in write:
#                     json.dump(i, fp=JSON_file, ensure_ascii=False, indent=2)
#         except BaseException as err:
#             print(err)
#             print(os.getcwd())  # 顯示路徑


class WedTool():

    def __init__(self, file_path, URL=None):

        self.__file_path = os.path.join(file_path)
        # self.file = self.readJSON(self.__file_path)

        self.readJSON()  # creat self.file
        self.__URL_analysis()  # creat self.URL

        self.__wed_code = "尚未執行reqURL(),回傳str"
        self.__html_goal = "尚未執行html_analysis(),回傳list"
        self.__css_goal = "尚未執行css_analysis(),回傳list"

    def get_url(self):
        return self.__URL.geturl()

    def get_wed(self):
        return self.__wed_code

    def get_html(self):
        return self.__html_goal

    def get_css(self):
        return self.__css_goal

    def get_file(self):
        return self.__file

    def get_file_path(self):
        return self.__file_path

    def readJSON(self):
        with open(self.__file_path, mode='r', encoding='utf-8') as JSON_file:
            self.__file = json.load(JSON_file, strict=False)

    def autoComplate(self):

        self.reqURL()
        self.html_analysis()
        self.css_analysis()

        string = ""

        for i in self.__css_goal:
            string = string + '<link rel="stylesheet" href="' + str(i) + '">'

        for i in self.__html_goal:
            string = string + str(i)

        string = string.strip('[')
        string = string.strip(']')

        return string

    def __URL_analysis(self):

        url = self.__file["info"]["URL"]

        self.__URL = urlparse(url)

    def reqURL(self):
        self.__wed_code = requests.get(self.__URL.geturl())
        if self.__wed_code.status_code == requests.codes.ok:
            self.__wed_code = BeautifulSoup(
                self.__wed_code.content, 'html.parser')

    # def html_analysis(HTMLcode, HTMLtag=None, searchTag=None, searchString=None, onlyChildren=False):
    def html_analysis(self):
        # onlyChildren只有尋找子節點，不含子孫節點

        def __keyExistDict(dictionary, key):
            return dictionary[key] if (key in dictionary) else None

        def step_analysis(code_origan,
                          html_tag=None,
                          search_tag=None,
                          search_string=None,
                          only_children=False):
            code_analysed = []
            for code in code_origan:
                code_analysed = code.find_all(
                    name=html_tag,
                    attrs=search_tag,
                    string=search_string,
                    recursive=(not only_children)
                )
                # goal = code.find_all( name = tag , attrs={key,value} , id= idTag ,class_= classTag ,href = hrefTag , recursive=!onlyChildren , string , **kwargs )
            return code_analysed

        code_analysed = []
        code_analysed.append(self.__wed_code)
        for method in self.__file["method"]:
            code_analysed = step_analysis(
                code_analysed,
                __keyExistDict(method, "HTMLtag"),
                __keyExistDict(method, "searchTag"),
                __keyExistDict(method, "searchString"),
                __keyExistDict(method, "onlyChildren")
            )

        self.__html_goal = code_analysed

        self.link_analysis()

    def css_analysis(self):
        css_analysis = self.__wed_code.find_all(
            name="link", attrs={"rel": "stylesheet"})

        self.__css_goal = []
        for code in css_analysis:
            self.__css_goal.append(urljoin(self.get_url(), code["href"]))
        style = self.__css_goal
        if style:
            self.__css_goal.extend(style)

    def link_analysis(self):
        for i in [['a', 'href'], ['img', 'src']]:
            x = self.__html_goal[0].find_all(i[0])
            new_string = ""
            html_goal_str = str(self.__html_goal)
            # print(str(x))

            for code in x:
                new_string = urljoin(self.get_url(), code[i[1]])
                # print(new_string)
                html_goal_str = html_goal_str.replace(
                    str(code[i[1]]), new_string)
                # print(str(code["href"]))

            self.__html_goal = []
            self.__html_goal.append(
                BeautifulSoup(html_goal_str, 'html.parser'))

            # print(str((self.__html_goal).find_all("a")))


if __name__ == "__main__":

    def WedTool_Test(self):
        print("--------")
        self.reqURL()
        self.html_analysis()
        self.css_analysis()
        self.link_analysis()

        # print("self.wed_code = " + str(self.get_url()))
        # print("self.wed_code = " + str(self.get_wed()))
        # print("self.wed_code = " + str(self.get_html()))
        # print("self.wed_code = " + str(self.get_css()))
        # print("self.wed_code = " + str(self.get_file()))

        # print("reqURL() = " + self.wed_code)
        # print("self.file = " + self.file)
        # print("self.html_analysis = " + str(self.html_goal))  # is list

        # print("self.css_analysis = " + str(self.css_goal))

        print("--------")

    # code = WedTool(URL="https://dboyliao.medium.com")

    code = WedTool(
        file_path="School_Project\Heroku\Server Side\myproject\json\英檢_備考方法_全民英檢活動報.json")
    # WedTool_Test(code)
    print(code.autoComplate())
