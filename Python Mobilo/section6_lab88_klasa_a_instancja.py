class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        Cake.bakery_offer.append(self)

    def show_info(self):
        print(self.name.upper())
        print("Taste: {}".format(self.taste))
        print("The kind: {}".format(self.kind))
        if len(self.addictions) > 0:
            print("Addictions:")
            for ad in self.addictions:
                print("- {}".format(ad))
        if self.filling:
            print("The filling: {}".format(self.filling))
        print("-" * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, list_of_additives):
        for additive in list_of_additives:
            self.addictions.append(additive)


muffin = Cake('Muffin', 'muffin', 'sweet', ["chocolate"], 'chocolate')
tarta = Cake("Tarta", 'cake', 'sweet', ["strawberries", "cream"], "jam")
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')
ice_cake = Cake('Ice Cake', 'cake', 'very sweet', ['chocolate', 'ice'], '')


print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()


print('Is cake04 of type Cake? (isinstance)', isinstance(cake04, Cake))
print('Is cake04 of type Cake? (type)', type(cake04) is Cake)
print('vars cake04', vars(cake04))
print('vars Cake?', vars(Cake))
print('dir cake04', dir(cake04))
print('dir Cake?', dir(Cake))
