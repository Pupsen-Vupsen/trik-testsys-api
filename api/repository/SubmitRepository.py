from api.model.Submit import Submit


class SubmitRepository:
    @classmethod
    def init_repository(cls) -> None:
        Submit.create_table()

    @classmethod
    async def get_student_submits(cls, student_id: str) -> list[Submit]:
        return Submit.select().where(Submit.student_id == student_id)

    @classmethod
    def drop_table(cls):
        Submit.drop_table()
