"""
* class는 설계도다, 객체는 독립적이다

4원칙: 캡슐화, 추상화, 상속, 다형성

"""

# 사칙연산 프로그램 만들기
# 계산기를 만드는것을 통해 구현


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def dev(a, b):
    return a / b


# print(sub(1, 2))
# print(add(1, 2))
# print(mul(1, 2))


# class를 짜는 생각 흐름
# 절차 지향적으로 먼저 짜고
# 반복되는 무언가를 캐치
# 행위를 나누고 속성을 나눌수 있는지 확인


class Calc:

    # 생성자: 객체 찍을때 가장 먼저 실행
    # self = 객체를 지칭
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def dev(self):
        return self.a / self.b


calc1 = Calc(1, 2)

# Calc1에는 네임 스페이스라는 공간이 생김
# 그 공간에는 a, b변수와 사칙연산 메소드가 존재

print(calc1.add())

calc1.a = 7  # 필드 재조정 가능

print(calc1.add())
