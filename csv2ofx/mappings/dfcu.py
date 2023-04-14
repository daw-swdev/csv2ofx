from operator import itemgetter

mapping = {
    "has_header": True,
    "is_split": False,
    "bank": "Digital Federal Credit Union",
    "bank_id": "211391825",
    "currency": "USD",
    "date": itemgetter("DATE"),
    "type": itemgetter("TRANSACTION TYPE"),
    "payee": itemgetter("DESCRIPTION"),
    "amount": itemgetter("AMOUNT"),
    "id": itemgetter("ID"),
    "notes": itemgetter("MEMO"),
}
