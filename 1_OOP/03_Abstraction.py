"""
추상화
불필요한 정보는 숨기고 필요한 정보만을 표현
공통의 속성값, 행위들을 하나로 묶어 이름 붙이는것
"""

siri_name = "siri"
siri_code = 1234213


def siri_say_hi():
    # code ...
    print("반갑습니다")


def siri_calc_add():
    return 2 + 3


def siri_die():
    # code ...
    print("초기화 되었습니다")


javis_name = "javis"
javis_code = 3222134


def javis_say_hi():
    # code ...
    print("Hi")


def javis_calc_add():
    return 9 + 5


def javis_die():
    # code ...
    print("삭제 되었습니다")


# 로봇으로 추상화


class Robot:

    # class 변수
    current_robot_count = 0

    # 데코레이터 문법 사용
    @classmethod
    def how_many(cls):
        print(f"current robot count = {cls.current_robot_count}")

    def __init__(self, _name, _code) -> None:
        self.name = _name
        self.code = _code
        Robot.current_robot_count += 1

    def say_hi(self):
        print(f"hi I'm {self.name}!")

    def calc_add(self, _a, _b):
        return print(_a + _b)

    def die(self):
        Robot.current_robot_count -= 1
        print(f"{self.name} is died!")
        Robot.how_many()


print(Robot.current_robot_count)

siri = Robot("siri", 123124)
print(Robot.current_robot_count)
javis = Robot("javis", 412324)
print(Robot.current_robot_count)
bixby = Robot("bixby", 5993)
print(Robot.current_robot_count)


siri.say_hi()
javis.say_hi()

bixby.calc_add(3, 6)

print(Robot.how_many())

siri.die()