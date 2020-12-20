import requests
from bs4 import BeautifulSoup

import json
import os


def reqURL(URI):
    wed = requests.get(URI)
    if wed.status_code == requests.codes.ok:
        wed = BeautifulSoup(wed.text, 'html.parser')
        return wed


def analysis(HTMLcode, HTMLtag=None, searchTag=None, searchString=None, onlyChildren=False):
    # onlyChildren只有尋找子節點，不含子孫節點
    goal = []
    for code in HTMLcode:
        goal = code.find_all(
            name=HTMLtag, attrs=searchTag, string=searchString, recursive=(not onlyChildren))
        # goal = code.find_all( name = tag , attrs={key,value} , id= idTag ,class_= classTag ,href = hrefTag , recursive=!onlyChildren , string , **kwargs )
    return goal


def readJSON(path):
    try:
        with open(path, mode='r', encoding='utf-8') as JSON_file:
            return json.load(JSON_file)

    except BaseException as err:
        print(err)
        print(os.getcwd())  # 顯示路徑


def writeJSON(path, write):
    try:
        with open(path, mode='w', encoding='utf-8') as JSON_file:
            for i in write:
                json.dump(i, fp=JSON_file, ensure_ascii=False, indent=2)
    except BaseException as err:
        print(err)
        print(os.getcwd())  # 顯示路徑


def css_analysis(URL, HTMLcode):
    css_list = HTMLcode.find_all(name="link", attrs={"rel": "stylesheet"})
    if ("." in URL.split("/")[-1]):
        URL_list = URL.split("/")
        URL_list[-1] = ""
        string = ""
        for i in URL_list:
            string = string + i + "/"
        URL = string[:-1]
    for (i, value) in enumerate(css_list):

        css_URL = URL + value["href"]
        css_list[i] = f'<link rel="stylesheet" href="{css_URL}">'

    return css_list


if __name__ == "__main__":

    URL = "https://www.gept.org.tw/GEPT1/gepttestdate.aspx"
    if ("." in URL.split("/")[-1]):
        URL_list = URL.split("/")
        URL_list[-1] = ""
        string = ""
        for i in URL_list:
            string = string + i + "/"
        URL = string[:-1]
    print(URL)
