from abc import ABCMeta # 파이썬의 객체지향 인터페이스로 선언
from user.domain.user import User

# User 도메인을 영속화하기 위한 모듈, 첫글자 I는 인터페이스를 의미
class IUserRepository(metaclass=ABCMeta):
    @abstractmethod # 인터페이스의 구현체에서 구현할 함수 선언
    def save(self, user: User):
        raise NotImplementedError # 구현부에서 구현이 필요함을 알림.