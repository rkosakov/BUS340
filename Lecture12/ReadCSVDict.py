import csv

with open('employee_birthday.csv', mode='r') as cvs_file:

    csv_reader = csv.DictReader(cvs_file)

    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1

        print(f'\t {row["name"]} works in the {row["department"]} department and was born in {row["birthday mouth"]}')
        line_count += 1

print(f'Processed {line_count} lines.')


