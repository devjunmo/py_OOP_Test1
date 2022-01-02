# decorator: 함수


def copyright(func):
    def new_func():
        print("@ copyright:afdjodsifja230942")
        func()

    return new_func


@copyright
def smile():
    print("😁")


@copyright
def angry():
    print("😫")


@copyright
def love():
    print("😍")


# # 함수 재 정의 -> @ 문법으로 대체
# smile = copyright(smile)
# angry = copyright(angry)
# love = copyright(love)


smile()
angry()
love()
