from api.model.Submit import Submit


class SubmitRepository:

    @classmethod
    def init_repository(cls):
        Submit.create_table()

    @classmethod
    async def get_student_submits(cls, student_id: str) -> list[Submit]:
        return Submit.select().where(Submit.student_id == student_id)
