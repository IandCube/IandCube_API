from myproject import model


def value():
    english = model.WedCreator(
        "Heroku\Server Side\\myproject\json\demo1.json")
    english.reqvalueFromURL()
    return english.value


if __name__ == "__main__":

    english = model.WedCreator(
        "Education-Project\web\網頁調適\Server Side\Crawler\demo1.json")
    english.reqvalueFromURL()
    print(english.value)
