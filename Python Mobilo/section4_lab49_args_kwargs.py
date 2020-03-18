# zadanie 1


def calculate_paint(efficency_ltr_per_m2, *args):
    total = 0
    for arg in args:
        total = total + efficency_ltr_per_m2 * arg
    print("Potrzeba {} litrów farby".format(total))


calculate_paint(12, 34, 45, 21)
rooms = [34, 45, 21]
calculate_paint(12, *rooms)


# zadanie 2


def log_it(*args):
    path = r'/home/krysia/kursy/Python Mobilo/log_it.txt'
    with open(path, "a") as file:
        for arg in args:
            file.write(arg + ' ')
        file.write("\n")


log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')