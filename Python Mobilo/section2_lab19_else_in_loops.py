import os
import urllib.request

data_dir = r'/home/krysia/kursy/Python Mobilo/'
pages = [

    {'name': 'mobilo', 'url': 'http://www.mobilo24.eu/'},

    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/'},

    {'name': 'kursy', 'url': 'http://www.kursyonline24.eu/'}]

print("-----------------")
for page in pages:
    try:
        path = data_dir + page['name'] + ".html"
        urllib.request.urlretrieve(page['url'], path)
        print(path)
    except:
        print('Failure ' + page['name'])
        break
else:
    print("all pages downloaded sucessfully")
