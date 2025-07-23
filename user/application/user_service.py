from ulid import ULID
from datetime import datetime
from user.domain.user import User
from user.domain.repository.user_repo import IUserRepository
from user.infra.repository.user_repo import UserRepository

class UserService:
    def __init__(self):
        self.user_repo: IUserRepository = UserRepository() # 유저를 데이터베이스에 저장하는 저장소는 인프라 계층에 구현체가 존재해야 함.
        self.ulid = ULID()

    def create_user(self, name: str, email: str, password: str):
        now = datetime.now()
        user: User = User( # User 도메인 객체 생성
            id=self.ulid.now()
            name=name,
            email=email,
            password=password,
            created_at=now,
            updated_at=now,
        )
        self.user_repo.save(user) # 생성된 User 객체를 저장소에 전달하여 저장

        return user