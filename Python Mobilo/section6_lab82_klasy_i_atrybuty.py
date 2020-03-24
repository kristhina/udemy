class Cake:
    def __init__(self, name, kind, taste, addictions, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.filling = filling


muffin = Cake('Muffin', 'cake', 'sweet', ["chocolate"], 'chocolate')
tarta = Cake("Tarta", 'cake', 'sweet', ["strawberries", "cream"], "jam")

bakery_offer = [muffin, tarta]

print("Today in our offer:")
for cake in bakery_offer:
    print("{} - ({}), main taste: {}, with additves of: {}, filled with {}".format(cake.name, cake.kind, cake.taste,
                                                                                   cake.addictions, cake.filling))
