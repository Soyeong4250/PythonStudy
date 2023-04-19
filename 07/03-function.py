def test(msg):
    print(f"test함수 {msg} 호출")

def test1(msg = "안녕하세요"):
    print(f"test함수 {msg} 호출")

def test2(*a):  # positional argument : 인자가 몇 개일지 모를 때 사용
    print(f"{a}")

def test3(**a):  # keyword argument : 인자에 값을 전달할 대, 이름을 붙여서 전달하는 방식 (dictionary 자료형과 유사)
    print(f"{a}")

test("안녕하세요")
test1()
test2("aaa", "bbb", "ccc")
test3(name = "aaa")
