#def 와 if의 차이.
#def(인자)를 통한  함수.
#if 가정문
test = [
    {
        'name': 'aaa',
        'number': 10101,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'bbb',
        'number': 10102,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'ccc',
        'number': 10103,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'ddd',
        'number': 10104,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    },
    {
        'name': 'eee',
        'number': 10105,
        'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
        'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    }
]
test = [[1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
 [1, 5, 3, 4, 5, 1, 2, 3, 1, 2],
 [4, 3, 4, 4, 5, 3, 1, 2, 2, 4],
 [1, 3, 4, 4, 5, 3, 1, 2, 3, 2],
 [1, 3, 5, 4, 5, 3, 1, 2, 3, 4]];
a = [1, 5, 2, 4, 5, 3, 1, 2, 3, 4]
correct_answer = [1, 5, 2, 4, 5, 3, 1, 2, 3, 4]
student_answer = [1, 5, 2, 4, 5, 3, 1, 2, 3, 4]
for (student, correct) in zip(a, correct_answer):
     print(student , '/' , correct)

#구상: if 문을 통해 correct_answer와 같다면 100점
# 인덱스를 통해 리스트와 correct의 값을 비교해 값이 다르다면 -10점씩 차감한다.
#한다는 아이디어 까지는 생각해 봤는데 구상법을 모르겠습니다.


score = 0
for (student, correct) in zip(a, correct_answer):
    def get_score(student_answer, correct_answer):
        # 학생의 점수구하기 한 문항당 10점이라 가정.
        score = 0
        for (student, correct) in zip(student_answer, correct_answer):
            if student == correct:
                score = score + 10
        return score


    score = get_score(student_answer, correct_answer)
    print(score)

correct_answer = {
    'math': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'korean': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'english': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
    'science': [1, 3, 2, 4, 5, 3, 1, 2, 3, 4],
}
for student in test:
    math_score = get_score(student['math'], correct_answer['math'])
    korean_score = get_score(student['korean'], correct_answer['korean'])
    english_score = get_score(student['english'], correct_answer['english'])
    science_score = get_score(student['science'], correct_answer['science'])

    print("수학점수:", math_score)
    print("국어점수:", korean_score)
    print("영어점수:", english_score)
    print("과학점수:", science_score)

print("학생", student['name'], "==================")

# 답안의 key 기준으로 반복하는 방법
for key in correct_answer.keys():
    score = get_score(student[key], correct_answer[key])
    print(key, ": ",score)

# student key 기준으로 반복하는 방법
# for key in student.keys():
#     if key == 'name' or key == 'number':
#         continue
#     score = get_score(student[key], correct_answer[key])
#     print(key, ": ",score)