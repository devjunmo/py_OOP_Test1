"""
1. 파이썬에서 모든것은 개체이다. 함수도 개체임
"""


class Robot:

    """
    [Robot Class]
    Date : ??:??:??
    Author : Amaco
    """
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}.")

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        return f"We have {cls.population} robots."

    @staticmethod
    def are_you_robot():
        print("yes!!")

    # str 메소드 커스터마이징
    def __str__(self):
        return f"{self.name} robot!!"

    # call 메소드 커스터마이징
    def __call__(self):
        print("call!")
        return f"{self.name} call!!"


droid1 = Robot("R2-D2")
droid1.say_hi()

print(dir(droid1))

# 파이썬에서 모든것은 개채이다.
# 함수또한 개체이다
# 

print(droid1)  # 어떻게든 유저에게 문자열로 표현함
# 커스텀 후에는 오버라이팅 한것으로 나옴
# <__main__.Robot object at 0x7fde1c742110> -> R2-D2 robot!!


print(droid1())  # TypeError: 'droid1' object is not callable
# 당연히 callable하지 않는걸 ()로 call했으니 에러
# magic mtd __call__을 커스터마이징 해주면 call가능

