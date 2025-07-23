from abc import ABCMeta # 파이썬의 객체지향 인터페이스로 선언

# User 도메인을 영속화하기 위한 모듈, 첫글자 I는 인터페이스를 의미
class IUserRepository(metaclass=ABCMeta):
    pass