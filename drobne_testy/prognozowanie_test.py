import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

dane = pd.read_excel('BWUK.xlsx')
print(dane.shape)


y = dane['BWUK']
x = dane['okres'].values.reshape(-1,1)
print(y, x)
reg = LinearRegression()
reg.fit(x,y)
print("reg score")
print(reg.score(x,y))
print("reg coef")
print(reg.coef_)
print("reg intercept")
print(reg.intercept_)

x_prog = np.arange(37,46).reshape(-1,1)
print(x_prog)

prediction = reg.predict(x_prog)
print(prediction)

dane2 = pd.read_excel('BWUK_2020.xlsx')

dane2['prediction'] = prediction
dane2['difference'] = dane2['BWUK']-dane2['prediction']
print(dane2)

dane3 = pd.read_excel('ograniczenia.xlsx')
print(dane3)

result = pd.merge(dane2,dane3, on=dane2.index)
print(result)

y2 = result['difference']
x2 = dane3
reg2= LinearRegression(fit_intercept=False)
reg2.fit(x2,y2)
print("reg score")
print(reg2.score(x2,y2))
print("reg coef")
print(reg2.coef_)
print("reg intercept")
print(reg2.intercept_)
