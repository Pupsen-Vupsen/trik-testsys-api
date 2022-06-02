from api.model.User import User


class UserRepository:

    @classmethod
    def init_repository(cls) -> None:
        User.create_table()

    @classmethod
    async def create_user(cls, user_id: str, role: str) -> None:
        User.create(user_id=user_id, role=role)

    @classmethod
    async def get_user(cls, user_id: str) -> User | None:
        return User.get_or_none(User.user_id == user_id)
