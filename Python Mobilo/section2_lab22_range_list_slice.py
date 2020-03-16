colours_list = ["red", "orange", "green", "violet", "blue", "yellow"]


def number_of_colours(list_of_colours, n):
    new_list = list_of_colours[0:n]
    return new_list


for i in range(len(colours_list) + 1):
    print(number_of_colours(colours_list, i))

text = "Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli."
beginning = text.index("(")
ending = text.index(")")
wanted_text = text[beginning + 1:ending]
print(wanted_text)
