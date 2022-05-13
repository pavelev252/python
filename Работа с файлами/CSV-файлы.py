import csv
with open("sta.csv", "w") as c:
    w = csv.writer(c, delimiter=",")

    w.writerow(["oдин",
                "два",
                "три"])
    w.writerow(["Четыре",
                "пять",
                "шесть"])
