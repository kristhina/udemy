import os

files_to_process = [
    r'/home/krysia/kursy/Python Mobilo/helpers/script1.py',
    r'/home/krysia/kursy/Python Mobilo/helpers/script2.py',
]

for file in files_to_process:
    print(os.path.basename(file))
    f = open(file, "r")
    source = f.read()
    exec(source)
    f.close()