money = 0

while True:
  money = int(input("만원 이상의 금액을 입력해주세요 : "))
  if money < 10000:
    print("금액을 다시 입력해주세요")
  else: 
      print("만원권 : ", money // 10000)
      money %= 10000
      print("오천원권 : ", money // 5000)
      money %= 5000
      print("천원권 : ", money // 1000)
      money %= 1000
      print("오백원 : ", money // 500)
      money %= 500
      print("벡원 : ", money // 100)
      money %= 100
      print("십원 : ", money // 10)
      money %= 10
      break