"""
1. self는 인스턴스 객체이다.
2. 클래스 안에 있는 self의 주소와 만들어진 인스턴스의 주소는 같다.
    즉, self는 인스턴스 그 자체이다.
"""


class SelfTest:

    # class var
    name = "amamov"

    def __init__(self, _x):
        self.x = _x

    # class mtd
    @classmethod
    def func1(cls):
        print(f"cls: {cls}")
        print("func1")

    # instance mtd
    def func2(self):
        print(f"self: {self}")
        print(f"class 안의 self 주소: {id(self)}")
        print("func2")


test_obj = SelfTest(17)

print(f"인스터느의 주소: {id(test_obj)}")
test_obj.func2()
SelfTest.func1()

test_obj.func1()  # 실행 됨, 클래스 네임스페이스 찾아가서 cls 출력임
# 통상적으로 인스턴스에서 클래스 메소드를 호출하는건 어색함

print(test_obj.name)  # 클래스 네임스페이스 참고해서 출력해줌

try:
    SelfTest.func2()  # 당연히 안됨. self가 지정되지 않았으니까
except TypeError:
    print("타입 에러 발생")

SelfTest.func2(test_obj)  # self를 줬으니 당연히 됨

