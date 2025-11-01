frorom playground import user_input

score = int(input("점수를 입력하세요: "))

if score > 100 or score < 0:
    print("정상적인 점수범위가 아닙니다")
else:
    if score >= 80:
        print("합격입니다")
    elif score >= 60:
        print("재시험 응시가 필요합니다")
    else:
        print("불합격입니다")


input_unmder = int(input("숫자를 입력하세요"))
index = 1
while index < input_number:
    print(index)
    index = index + 1

input_number = int(input("숫자를 입력하세요: "))
index = 1
while index < input_number:
   if index % 2 == 0:
       print(index)
       index = index + 1
print("피보나치 수열")
list = [1,1]
lasat_item = list[len(list)-1]
while list_item <= input_unmder:
print(last_item)
list.append(lasat_item + list[len(list)-2]
lasat_item = [