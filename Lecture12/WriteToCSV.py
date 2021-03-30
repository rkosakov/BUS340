import csv

headers = ["IdNum", "Name", "CapitalCity", "Currency"]

rows = [str(50), "Italy", "Rome", "EUR",
        str(66), "Portugal", "Lisbon", "EUR"]

f = open("SBTable.csv", 'w')
f_csv = csv.writer(f)
f_csv.writerow(headers)
f_csv.writerows(rows)
f.close()