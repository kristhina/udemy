import csv

with open('/home/krysia/kursy/Python Mobilo/helpers/file1.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    while True:
        try:
            print(next(csvreader))
        except StopIteration:
            break
    print("All lines have been printed")
