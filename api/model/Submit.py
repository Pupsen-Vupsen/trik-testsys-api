import peewee as pw


class Submit(pw.Model):
    submit_id: pw.CharField = pw.CharField(unique=True, primary_key=True)
    student_id: pw.CharField = pw.CharField()
    task_name: pw.CharField = pw.CharField()
    result: pw.CharField = pw.CharField()

    class Meta:
        database: pw.SqliteDatabase = pw.SqliteDatabase("/data/submit.sqlite", pragmas={
            'journal_mode': 'wal',
            'synchronous': 'normal'
        })
