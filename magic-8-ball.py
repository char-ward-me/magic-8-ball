import csv
import random


print('''
Welcome to the Magic 8 Ball!
''')

question = input("Ask me any question ")

with open("answers.csv", encoding = "utf-8") as all_csv:
    reader = csv.reader(all_csv)
    all_answers = list(reader)

answer = random.choice(all_answers[0])

print(answer)
