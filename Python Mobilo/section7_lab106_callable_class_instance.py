class NoDuplicates:
    def __init__(self):
        self.my_list = []

    def __call__(self, new_items):
        for item in new_items:
            if item not in self.my_list:
                self.my_list.append(item)


my_no_dup_list = NoDuplicates()
print(my_no_dup_list.my_list)

my_no_dup_list(['keyboard', 'mouse'])
print(my_no_dup_list.my_list)

my_no_dup_list(['keyboard', 'mouse', 'pendrive'])
print(my_no_dup_list.my_list)

my_no_dup_list(['charger', 'pendrive'])
print(my_no_dup_list.my_list)