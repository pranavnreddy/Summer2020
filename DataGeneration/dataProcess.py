import csv


def setup():
    first_names = []
    last_names = []

    with open('Popular_Baby_Names.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                first_names.append(row[3])
                line_count += 1
        print(f'Processed {line_count} lines.')

    with open('Names_2010Census.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                last_names.append(row[0])
                line_count += 1
        print(f'Processed {line_count} lines.')


    first_names_file = "first_names.csv"
    last_name_file = "last_names.csv"

    with open(first_names_file, mode='w') as csv_file:
        fieldnames = ['name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for name in first_names:
            writer.writerow({'name': name})

    with open(last_name_file, mode='w') as csv_file:
        fieldnames = ['name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for name in last_names:
            writer.writerow({'name': name})

def getCsvAttribute(filename, attribute, target_file):
    data = []
    fieldnames = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                fieldnames = row[attribute]
                line_count += 1
            elif row[attribute] != '':
                data.append(row[attribute])
                line_count += 1
        print(f'Processed {line_count} lines.')

    with open(target_file, mode='w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=[fieldnames])
        writer.writeheader()
        for element in data:
            writer.writerow({fieldnames: element})

def main():
    getCsvAttribute('statewide.csv', 2, 'street_numbers.csv')

if __name__ == "__main__":
    main()