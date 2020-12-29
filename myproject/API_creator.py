from myproject import model_Fun as model


def page2_1_b_a():
    english = model.WedTool(
        "myproject/json/英檢_報名日期_考試通知查詢列印.json")
    return english.autoComplate()


def page2_1_b_b():
    english = model.WedTool(
        "myproject/json/英檢_報名日期_測驗日程.json")
    return english.autoComplate()


def page2_1_b_c():
    english = model.WedTool(
        "myproject/json/英檢_成績查詢_成績查詢.json")
    return english.autoComplate()


# def demo4():
#     english = model.WedTool(
#         "myproject/json/英檢_備考方法_全民英檢活動報.json")
#     return english.autoComplate()


# def demo5():
#     english = model.WedTool(
#         "myproject/json/英檢_備考方法_全民英檢電子報.json")
#     return english.autoComplate()


if __name__ == "__main__":

    print(value())
