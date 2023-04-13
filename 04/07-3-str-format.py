a = 1234
b = 10.1
z = "a 변수의 값은 %d 이고, b는 %f" % (a, b)
print(z)

a = 1234
b = 10.1
x = "a 변수의 값은 {} 이고, b는 {}".format(a, b)
y = "b 변수의 값은 {1} 이고, a는 {0}".format(a, b)
print(x)
print(y)

c = "     안녕     "
d = "{: ^30}".format("안녕") + "!" # 양쪽에 공백 30개 삽입하고 가운데에 문자열 출력 (가운데 정렬)
e = "{:->30}".format("안녕") + "!" # 우측으로 -기호를 30개 출력한 후 문자열 출력
f = "{:,}".format(123456789) # 3자리 수마다 ,찍기
print(c)
print(d)
print(e)
print(f)