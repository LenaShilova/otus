import json
import csv
from csv import DictReader

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

with open(RESULT_FILE, "w") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)