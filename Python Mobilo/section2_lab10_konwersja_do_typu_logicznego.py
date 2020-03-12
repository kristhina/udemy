options = ['load data', 'export data', 'analyze & predict']

choice = 'x'


def DisplayOptions(list_of_options):
    for i in range(len(list_of_options)):
        print(str(i+1) +" " + list_of_options[i])
    print("------------------------------")
    return input("Select option above or press enter to exit")


while choice:
    try:
        choice = DisplayOptions(options)
        choice_num = int(choice)
        if 0 < choice_num < 4:
            print("You have chosen the option:'{}'".format(options[choice_num-1]))
        else:
            print("you should give a number: 1, 2 or 3")
    except ValueError:
        print("you should give a number: 1, 2 or 3")


