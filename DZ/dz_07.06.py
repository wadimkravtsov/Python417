import requests
import json
import csv

response = requests.get("https://jsonplaceholder.typicode.com/todos") # Скачали файл в виде строки
# print(type(response.text))
todos = json.loads(response.text) # Перевели в json формат
print(todos)

with open("todos_writer.csv", "w") as f:
    writer = csv.DictWriter(f, delimiter=';', lineterminator="\r", fieldnames=todos[0].keys())
    writer.writeheader()
    for t in todos:
        writer.writerow(t)