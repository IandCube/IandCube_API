from myproject import model


def value():
    english = model.WedCreator(
        "myproject/json/demo1.json")
    english.reqvalueFromURL()

    string = ""
    for i in english.value:
        string = str(i) + string
    for i in english.css:
        string = str(i) + string

    return string


if __name__ == "__main__":

    print(value())
