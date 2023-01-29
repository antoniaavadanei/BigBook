from datetime import date, timedelta
from random import randint
NO_SIMULATIOS =10000

date_ = date(2000, 1, 1)


def generateBirthays(n: int):
    birthdays = []
    for i in range(n):
        random_day = randint(0, 364)
        birthday = date_ + timedelta(days=random_day)
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    for i in range(len(birthdays) - 1):
        for j in range(i + 1, len(birthdays)):
            if birthdays[i] == birthdays[j]:
                return birthdays[i]


n = int(input("How many birthdays?"))

cnt = 0
for i in range(NO_SIMULATIOS):
    birthdays = generateBirthays(n)
    # print(birthdays)
    x = getMatch(birthdays)
    if x is not None:
        # print(x)
        cnt += 1
    # print(i, cnt)
print("In a group of {} people there is {} probability of birthday coincidence ".format(n, cnt/NO_SIMULATIOS*100))
