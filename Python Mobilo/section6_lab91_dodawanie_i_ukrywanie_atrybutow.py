class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, addictions, filling, gluten_free):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        self.__gluten_free = gluten_free
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
        if self.__gluten_free:
            print("This cake is gluten free")
        else:
            print("This cake is not gluten free")
        print("-" * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, list_of_additives):
        for additive in list_of_additives:
            self.addictions.append(additive)


muffin = Cake('Muffin', 'muffin', 'sweet', ["chocolate"], 'chocolate', False)
tarta = Cake("Tarta", 'cake', 'sweet', ["strawberries", "cream"], "jam", False)
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False)
ice_cake = Cake('Ice Cake', 'cake', 'very sweet', ['chocolate', 'ice'], '', True)


print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()

# doda nowy atrybut i będą dwa różne gluten_free
cake04.__gluten_free = True
print(dir(cake04))
cake04.show_info()

# zmieni ciastko na gluten free
cake04._Cake__gluten_free = True
print(dir(cake04))
cake04.show_info()
