# Zapisz poniższe polecenie if w postaci uproszczonej:

price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

print('-----------------------')

# rozwiązanie:
price = 123
bonus = 23
bonus_granted = True

price = price-bonus if bonus_granted else price
print(price)

print('----------------------------')

# Zapisz poniższe polecenie if w postaci uproszczonej:

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('---------------------')

# rozwiązanie:
print('very good') if rating == 5 else print('good') if rating==4 else print('weak')

print('---------------------')

# Napisz program, który:
#
#     zapisze w zmiennej today_weekday nazwę dzisiejszego dnia tygodnia
#
#     bazując na pierwszej zwrotce piosenki serią poleceń if/elif/.../else ustali co dzisiaj powinieneś robić
#
# Przepisz powyższy program stosując składnie uproszczona polecenia if



import datetime as dt

today_weekday = dt.date.today().strftime("%A")

if today_weekday == 'Monday':
    print("pomagam mamie")
elif today_weekday == 'Tuesday' or today_weekday == 'Wednesday':
    print("ty masz w domu pranie")
elif today_weekday == 'Thursday':
    print("ja mam dyżur")
elif today_weekday == 'Friday':
    print("dwa zebrania")
elif today_weekday == 'Saturday':
    print("ty na lekcje ganiasz")
else:
    print("będzie dla nas")

print("pomagam mamie" if today_weekday == 'Monday' else
      "ty masz w domu pranie" if today_weekday == 'Tuesday' or today_weekday == 'Wednesday' else
      "ja mam dyżur" if today_weekday == 'Thursday' else
      "dwa zebrania" if today_weekday == 'Friday' else
      "ty na lekcję ganiasz" if today_weekday == 'Saturday' else
      "będzie dla nas")
