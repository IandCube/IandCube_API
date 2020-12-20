from myproject import model


def value():
    english = model.WedCreator(
        "myproject/json/demo1.json")
    english.reqvalueFromURL()
    return english.value


if __name__ == "__main__":

    print(value())
