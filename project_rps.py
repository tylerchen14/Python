import random

c_point = 0
p_point = 0

while True:

    choices = ["剪刀", "石頭", "布"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("準備出拳，剪刀石頭布？")

    if computer == player:
        print("平手")
    elif player == "剪刀" and computer == "布":
        print("你贏了🤩")
        p_point += 1
    elif player == "石頭" and computer == "剪刀":
        print("你贏了🤩")
        p_point += 1
    elif player == "布" and computer == "石頭":
        print("你贏了🤩")
        p_point += 1
    else:
        c_point += 1
        print("你輸了🥹")

    print("你出：" + player)
    print("電腦出：" + computer)

    print("現在積分：" + str(p_point) + " vs " + str(c_point))

    play = input("想要再一場（y/n）？：").lower()

    if play != "y":
        break

print("遊戲結束")
