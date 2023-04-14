from operator import itemgetter


def get_type_from_trxn(trxn):
    return 'debit' if trxn["column_4"] != "" else 'credit'


def get_amount_from_trxn(trxn):
    return trxn["column_4"] if trxn["column_4"] != "" else trxn["column_5"]


mapping = {
    "has_header": False,
    "is_split": False,
    "bank": "M&T Bank",
    "bank_id": "022000046",
    "currency": "USD",
    "id": itemgetter("column_1"),
    "date": itemgetter("column_2"),
    "payee": itemgetter("column_3"),
    "type": get_type_from_trxn,
    "amount": get_amount_from_trxn,
}
