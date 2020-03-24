class Cake:
    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling

    def show_info(self):
        print(self.name.upper())
        print("Taste: {}".format(self.taste))
        if len(self.addictions) > 0:
            print("Addictions:")
            for ad in self.addictions:
                print("- {}".format(ad))
        if self.filling:
            print("The filling: {}".format(self.filling))
        print("-"*30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, list_of_additives):
        for additive in list_of_additives:
            self.addictions.append(additive)


muffin = Cake('Muffin', 'cake', 'sweet', ["chocolate"], 'chocolate')
tarta = Cake("Tarta", 'cake', 'sweet', ["strawberries", "cream"], "jam")

bakery_offer = [muffin, tarta]

print("Today in our offer:")
for cake in bakery_offer:
    print("{} - ({}), main taste: {}, with additves of: {}, filled with {}".format(cake.name, cake.kind, cake.taste,
                                                                                   cake.addictions, cake.filling))

muffin.set_filling("chocolate cream")
tarta.add_additives(["raspberry", "milk"])


print("Today in our offer:")
for cake in bakery_offer:
    cake.show_info()