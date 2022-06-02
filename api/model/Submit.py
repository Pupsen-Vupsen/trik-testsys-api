from api.config import PATH_TO_SUBMITS
import peewee as pw


class Submit(pw.Model):
    submit_id: pw.CharField = pw.CharField(unique=True, primary_key=True)
    student_id: pw.CharField = pw.CharField()
    task_name: pw.CharField = pw.CharField()
    result: pw.CharField = pw.CharField()

    class Meta:
        database: pw.SqliteDatabase = pw.SqliteDatabase(
            PATH_TO_SUBMITS,
            pragmas={"journal_mode": "wal", "synchronous": "normal"},
        )
