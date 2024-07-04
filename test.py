def start_game():
    answer_sheet = []
    q_num = 0
    point = 0

    for k in questions:
        print("********")
        print(k)
        for i in options[q_num]:
            print(i)
        guess = input("你的答案是？").upper()
        answer_sheet.append(guess)

        point += check_answer(questions.get(k), guess)
        q_num += 1
    score(point, answer_sheet)


def check_answer(answer, guess):
    if answer == guess:
        print("答對了")
        return 1
    else:
        print("答錯了")
        return 0


def score(p, a):
    print("********")
    print("【成績單】")

    print("正確答案：", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("你的回答：", end="")
    for i in a:
        print(i, end=" ")
    print()

    score = int((p / len(questions)) * 100)
    print("你的分數是：" + str(score) + "%")


def play_again():
    response = input("是否再玩一次(yes/no)？").upper()
    if response == "YES":
        return True
    else:
        return False


questions = {
    "蜜蜂在採蜜時會跳舞，以此來傳達什麼訊息？": "A",
    "人體最長的肌肉是哪一個？": "C",
    "世界上最古老的寵物是什麼？": "B",
    "在太陽系中，最大的行星是什麼？": "B",
}

options = [
    [
        "A. 發現了美味的花蜜",
        "B. 發現了危險",
        "C. 告訴其他蜜蜂回到蜂巢",
        "D. 宣布天氣變化",
    ],
    ["A. 肱二頭肌", "B. 大腿肌肉", "C. 舌頭", "D. 腹肌"],
    ["A. 貓", "B. 狗", "C. 馬", "D. 鳥"],
    ["A. 地球", "B. 木星", "C. 火星", "D. 土星"],
]

start_game()

while play_again():
    start_game()
print("遊戲結束")
