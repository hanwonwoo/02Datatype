wonwoo = ["한원우", '27', '010-5233-****']
name = wonwoo[0]
age = wonwoo[1]
phone = wonwoo[2]

print(type(wonwoo))
print(name, age, phone)

names = [['한원우', '강수경', '강혜나',], ['20','21','22'], ['010-****-****','010-****-****','010-****-****']]
print(names[0][0:2])

numbers = [1,2,3,4,5]
result =numbers[2] = numbers[-1]
print(result)

print(len(names[0]))

#리스트에 요소 추가 및 제거하기
last = [1,2,3]
last.append(30)
print(last)
last.remove(3)
print(last)
print(type(last))

