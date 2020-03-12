a = b = c = 10
print(a, id(a))
print(b, id(b))
print(c, id(c))

a = 20

print(a, id(a))
print(b, id(b))
print(c, id(c))

a = b = c = [1, 2, 3]
a.append(4)

print(a, id(a))
print(b, id(b))
print(c, id(c))

x = 10
y = 10

print(x, id(x))
print(y, id(y))

y = y + 1
y = y - 1

print(x, id(x))
print(y, id(y))

y += 1234567890
y -= 1234567890

print(x, id(x))
print(y, id(y))
