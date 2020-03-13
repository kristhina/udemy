import os

f = open('first_file.txt', 'w+')
for i in range(10):
    f.write("This is the line number {}".format(i+1))
f.close()

def len_file(file):
    f1 = open(file, 'r')
    file_text = f1.read()
    file_split = file_text.split()
    f1.close()
    return len(file_split)

leeeeen = len_file('first_file.txt')
print(leeeeen)


path = r'/home/krysia/kursy/Python Mobilo/first_file.txt'

if os.path.isfile(path):
    print("There are {} words in the file {}".format(len_file(path), path))

cwd = os.getcwd()
print(cwd)