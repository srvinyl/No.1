
import random

weapon_level = 0
upgrade_rates = [
    {"up": 70, "keep": 30, "down": 0, "break": 0},
    {"up": 60, "keep": 25, "down": 10, "break": 5},
    {"up": 50, "keep": 30, "down": 15, "break": 5},
    {"up": 45, "keep": 30, "down": 20, "break": 5},
    {"up": 40, "keep": 30, "down": 20, "break": 10},
    {"up": 35, "keep": 30, "down": 25, "break": 10},
    {"up": 30, "keep": 30, "down": 30, "break": 10},
    {"up": 25, "keep": 30, "down": 30, "break": 15},
    {"up": 20, "keep": 30, "down": 30, "break": 20},
    {"up": 15, "keep": 30, "down": 30, "break": 25},
    {"up": 0, "keep": 100, "down": 0, "break": 0}
]

while True:
    print("\n--- TFaRPG ---")
    choice = input("숫자를 입력하세요 (0을 입력하면 종료): ")

    if choice == "0":
        print('게임을 종료 합니다')
        break

    print("로비로 이동 합니다")
    G = input("숫자를 입력하세요 (1: 상점, 2: 던전, 3: 종료): ")

    if G == "3":
        print('게임을 종료 합니다')
        break

    if G == "1":
        print(f"\n현재 무기 레벨: {weapon_level}")
        confirm = input("무기를 강화할까요? (1: 예, 2: 아니오): ")

        if confirm == "1":

            rate = upgrade_rates[weapon_level]
            ran_num = random.randint(0, 99)

            print(f"강화 확률 정보: {rate}")


            if ran_num < rate["up"]:
                weapon_level += 1
                print(f"강화 성공! 현재 레벨: {weapon_level}")
            elif ran_num < rate["up"] + rate["keep"]:
                print("강화 유지되었습니다.")

        else:
            print("강화를 취소했습니다.")

    elif G == "2":
        print("던전에 입장합니다! (기능 미구현)")
