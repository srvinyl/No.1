import random

weapon_level = 0
boss_level = 0
is_dragon_slayer = False

boss_names = [
    "대갈이군", "야옹마", "맴매 선생", "쿠오리넨", "반역의 발키리",
    "폭주한 고양이 무트", "신", "신(진심)", "격*신", "악마 각하", "파괴신 자간드"
]

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


def show_status():
    print("\n" + "=" * 30)
    if is_dragon_slayer:
        print("[드래곤 처치자] 전설의 용사님, 환영합니다!")

    print(f"현재 무기 레벨: {weapon_level}")

    current_boss = boss_names[boss_level] if boss_level < len(boss_names) else "심연의 왕"
    print(f"도전 중인 보스: {current_boss} (Lv.{boss_level})")
    print("=" * 30)


def start_battle(w_lv, b_lv):
    level_diff = w_lv - b_lv

    if level_diff <= -3:
        win_rate = 0
    elif level_diff == -2:
        win_rate = 20
    elif level_diff == -1:
        win_rate = 30
    elif level_diff == 0:
        win_rate = 50
    elif level_diff == 1:
        win_rate = 70
    elif level_diff == 2:
        win_rate = 90
    else:
        win_rate = 100

    print(f"승리 확률: {win_rate}%!")

    dice = random.randint(0, 99)
    return dice < win_rate


while True:
    show_status()

    print("1. 무기 강화")
    print("2. 보스 도전")
    print("3. 종료하기")

    choice = input("원하는 행동을 선택하세요: ")

    if choice == "1":
        if weapon_level >= 10:
            print("이미 최고 레벨입니다.")
            continue

        rate = upgrade_rates[weapon_level]
        ran_num = random.randint(0, 99)

        if ran_num < rate["up"]:
            weapon_level += 1
            print(f"강화 성공! 현재 레벨: {weapon_level}")

        elif ran_num < rate["up"] + rate["keep"]:
            print("강화 실패: 레벨 유지")

        elif ran_num < rate["up"] + rate["keep"] + rate["down"]:
            weapon_level = max(0, weapon_level - 1)
            print(f"강화 실패: 레벨 하락 → {weapon_level}")

        else:
            weapon_level = 0
            print("강화 실패: 무기 파괴됨 (0으로 초기화)")

    elif choice == "2":
        if boss_level >= len(boss_names):
            print("이미 모든 보스를 처치했습니다!")
            continue

        print(f"\n⚔ {boss_names[boss_level]}에게 도전!")

        if start_battle(weapon_level, boss_level):
            print("보스 처치 성공!")

            if boss_level == 10:
                print("축하합니다! 모든 보스를 제압했습니다!")
                is_dragon_slayer = True

            boss_level += 1
        else:
            print("패배했습니다... 더 강화하세요.")

    elif choice == "3":
        print("게임을 종료합니다.")
        break

    else:
        print("잘못된 선택입니다.")










