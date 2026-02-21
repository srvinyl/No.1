1


while True:
    print("TFaRPG")
    choice = input("숫자를 입력하세요 (0을 입력하면 종료): ")

    if choice == "0":
        print('게임을 종료 합니다')
        break

    print("로비로 이동 합니다")
    G = input("숫자를 입력하세요 (1: 상점, 2: 던전, 3: 종료): ")

    if G == "3":
        print('게임을 종료 합니다')

    if G == "1":
        print("무기를 강화할까요?")
        L = input()
        break