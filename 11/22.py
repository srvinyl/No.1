#def 와 if의 차이.
#def(인자)를 통한  함수.
#if 가정문
#변수 = 저장소. 함수 = 어떤 역할이 부여된 저장소

a = [1, 5, 2, 4, 5, 3, 1, 2, 3, 4]
correct_answer = [1, 5, 2, 4, 5, 3, 1, 2, 3, 4]

for (student, correct) in zip(a, correct_answer):
     print(student , '/' , correct)

#구상:리스트를 만들고 if 문을 통해 correct_answer와 같다면 100점
# 인덱스를 통해 리스트와 correct의 값을 비교해 값이 다르다면 -10점씩 차감한다.
#한다는 아이디어 까지는 생각해 봤는데 구상법을 모르겠습니다.

