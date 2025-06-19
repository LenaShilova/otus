import json
import csv


BOOKS_FILE = "resources/books.csv"
USER_FILE = "resources/users.json"
RESULT_FILE = "resources/result.json"


with open(BOOKS_FILE, "r") as f:
    books = list(csv.DictReader(f))


with open(USER_FILE, "r") as f:
    users = json.load(f)


for user in users:
    user["books"] = []


user_index = 0
for book in books:
    users[user_index]["books"].append(book)
    user_index = (user_index + 1) % len(users)


result = [
    {
        "name": u["name"],
        "gender": u["gender"],
        "address": u["address"],
        "age": u["age"],
        "books": [
            {
                "title": b["Title"],
                "author": b["Author"],
                "pages": int(b["Pages"]),
                "genre": b["Genre"]
            }
            for b in u["books"]
        ]
    }
    for u in users
]

with open(RESULT_FILE, "w") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)