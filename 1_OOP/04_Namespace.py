"""
1. Namespace = 개채를 구분할 수 있는 범위
2. __dict__ : Namespace를 확인
3. dir(): Namespace의 key값 확인
4. __doc__: class의 주석 확인
5. __class__: 어떤 클래스로 만들어진 인스턴스인지 확인

"""


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


siri = Robot("siri", 123124)
print(Robot.current_robot_count)
javis = Robot("javis", 412324)
print(Robot.current_robot_count)
bixby = Robot("bixby", 5993)
print(Robot.current_robot_count)


print(Robot.__dict__)  # 클래스 네임스페이스에 인스턴스 메소드가 있음

print(siri.__dict__)  # 인스턴스 메소드 x, 메모리 효율문제로 클래스 네임스페이스에 있음

# siri.calc_add()
# 인스턴스 네임스페이스에 없는데 어떻게 호출?
# 인스턴스에 없으면 클래스로 가서 찾는다

# 이 원리로 인스턴스에서 클래스 변수로 접근 가능

print(siri.current_robot_count)  # 3
print(siri.how_many())  # current robot count = 3

# 파이썬에서
# Robot.say_hi()  # 이건 안됨. self 인자 없다는 오류나옴
Robot.say_hi(siri)  # 이건 당연히 됨. self는 객체고, 객체를 넣어줬으니까.



# dir()은 bulilt in이고 ,네임스페이스 정보를 사용자화 해서

print(dir(siri)) # 접근 가능한 목록들을 출력해줌

print(dir(Robot))



# __doc__은 클래스에 대한 주석 출력
# 이걸보고 남의 코드를 대략적 이해
print(Robot.__doc__)


# __class__는 객체가 어느 클래스로 만들어 졌는지
print(siri.__class__)