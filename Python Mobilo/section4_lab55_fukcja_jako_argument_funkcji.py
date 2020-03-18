def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2


def generate_values(name, my_list):
    new_list = []
    for number in my_list:
        new_list.append(name(number))
    return new_list


x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(root, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))