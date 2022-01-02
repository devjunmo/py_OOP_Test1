class Robot:

    """
    [robot class]

    Author: yang
    role: ???
    
    """

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

    # 자유로운 메소드
    def is_robot_class():
        print("yes")

    # 자유로운 메소드 - static mtd
    @staticmethod
    def is_robot_class_static():
        print("yes")


siri = Robot("siri", 123124)
print(Robot.current_robot_count)
javis = Robot("javis", 412324)
print(Robot.current_robot_count)
bixby = Robot("bixby", 5993)
print(Robot.current_robot_count)


# siri.is_robot_class() # error
Robot.is_robot_class()  # yes

siri.is_robot_class_static()  # yes
Robot.is_robot_class_static()  # yes
