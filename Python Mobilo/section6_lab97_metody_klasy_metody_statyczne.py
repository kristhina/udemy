import pickle
import glob


class Cake:
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, addictions, filling, gluten_free, text):
        self.name = name
        if kind in Cake.known_types:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.addictions = addictions
        self.filling = filling
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))
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
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print("-" * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, list_of_additives):
        for additive in list_of_additives:
            self.addictions.append(additive)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    def save_to_file(self, path_to_file):
        with open(path_to_file, "wb") as file:
            pickle.dump(self, file)
            print("done")

    @classmethod
    def read_from_file(cls, path_to_file):
        with open(path_to_file, "rb") as file:
            new_cake = pickle.load(file)
        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog_name):
        return glob.glob(catalog_name + "/*.bakery")


    Text = property(__get_text, __set_text, None, "Text on the cake")


muffin = Cake('Muffin', 'muffin', 'sweet', ["chocolate"], 'chocolate', False, 'lalala')
tarta = Cake("Tarta", 'cake', 'sweet', ["strawberries", "cream"], "jam", False, 'lelele')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, '')
ice_cake = Cake('Ice Cake', 'cake', 'very sweet', ['chocolate', 'ice'], '', True, '')


print("Today in our offer:")
for cake in Cake.bakery_offer:
    cake.show_info()

cake04.Text = "fadfafak"
ice_cake.Text = "nanananananabatman"

print(ice_cake.Text)


cake04.save_to_file(r'/home/krysia/kursy/Python Mobilo/cake04.bakery')
muffin.save_to_file(r'/home/krysia/kursy/Python Mobilo/c_muffin.bakery')

cake05 = Cake.read_from_file(r'/home/krysia/kursy/Python Mobilo/cake04.bakery')

cake05.show_info()

print(Cake.get_bakery_files(r'/home/krysia/kursy/Python Mobilo'))
