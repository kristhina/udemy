text_list = ['x', 'xxx', 'xxxxx', 'xxxxxxx', '']

f = lambda x: len(x)

print(f("aaa"))

for x in text_list:
    print(f(x))

map_text_list = list(map(f, text_list))
print(map_text_list)

print(list(map(lambda x: len(x), text_list)))
