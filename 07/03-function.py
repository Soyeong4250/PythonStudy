def test(msg):
    print(f"test함수 {msg} 호출")

def test1(msg = "안녕하세요"):
    print(f"test함수 {msg} 호출")

def test2(*a):  # positional argument : 인자가 몇 개일지 모를 때 사용
    print(f"{a}")

def test3(**a):  # positional argument : 인자가 몇 개일지 모를 때 사용
  print(f"{a}")

test("안녕하세요")
test1()
test2("aaa", "bbb", "ccc")
test3("aaa", "bbb", "ccc")
