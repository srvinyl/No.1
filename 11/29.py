#11월 29일 반복문
#continue = skip
# 조건을 뛰어넘는 역할
#key , value는 dictionary를 구성하는 역할.
import random


#Up Dawn 게임
#순서 정해서 생각해보자
#랜덤 함수로 무작위 값 정했으면 뭐가 다음에 필요함?
#사용자가 입력한 수와 랜덤 값을 비교해야지


import random

def updawn():
    resultn = random.randrange(1, 100)
print("숫자를 입력해 주세요")
resultn = input()
while True:
    vy = input()
    if vy < resultn:
        print("업")
    elif vy> resultn:
        print("다운")
    else:
        print("정답입니다.")
        break
