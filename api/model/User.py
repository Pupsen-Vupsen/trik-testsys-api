from api.config import PATH_TO_USERS
import peewee as pw


class User(pw.Model):
    user_id: pw.CharField = pw.CharField(unique=True, primary_key=True)
    telegram_id: pw.CharField = pw.CharField(unique=True)
    role: pw.CharField = pw.CharField()

    class Meta:
        database: pw.SqliteDatabase = pw.SqliteDatabase(
            PATH_TO_USERS,
            pragmas={"journal_mode": "wal", "synchronous": "normal"},
        )
