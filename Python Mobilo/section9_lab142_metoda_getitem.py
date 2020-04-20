class Combinations:

    def __init__(self, products, promotions, customers):
        self.products = products
        self.promotions = promotions
        self.customers = customers

    def __getitem__(self, item):
        if item >= len(self.promotions)*len(self.products)*len(self.customers):
            raise StopIteration
        else:
            pos_products = item // (len(self.promotions)*len(self.products))
            item = item % (len(self.promotions) * len(self.customers))
            pos_promotions = item // len(self.customers)
            item = item % len(self.customers)
            pos_customers = item
            return "{} - {} -{}".format(self.products[pos_products],
                                        self.promotions[pos_promotions],
                                        self.customers[pos_customers])




products = ["Product {}".format(i) for i in range(1, 4)]
promotions = ["Promotion {}".format(i) for i in range(1, 3)]
customers = ['Customer {}'.format(i) for i in range(1, 6)]

combinations = Combinations(products, promotions, customers)

for i in range(18):
    print(combinations[i])
print('-'*30)

combinations_iterator = iter(combinations)
print(next(combinations_iterator))
print(next(combinations_iterator))
print(next(combinations_iterator))
print(next(combinations_iterator))

print('+' * 30)

for c in combinations_iterator:
    print(c)
print('*'*30)

