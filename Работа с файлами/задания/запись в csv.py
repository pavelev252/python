import csv
list_12 = [["Звездные войны", "Терминатор", "Искуственный интелект"],
                ["Дурак", "Матильда ", "Левиафан"],
                ["Люди в черном", "Я - робот", "Эволюция"]]

with open("C:/Users/робот5/Desktop/отборочные/write.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=',')
    w.writerows(list_12)
