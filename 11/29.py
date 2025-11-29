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

from platground import user_input


def updawn():
    result = random.randrange(1, 100 )
    print("숫자를 입력해 주세요")
    vy_str = input()
    vy_int = int(vy_str)  # 입력받은 문자열을 정수로 변환

    if vy_int < 50:  # 정수형 변수 vy_int를 50과 비교
        print("Up")