lista = ['iphone', 'ipad', 'ipod', 'macbook', 'macpro']
valores = [100, 200, 300, 400, 500]

import matplotlib.pyplot as plt

plt.bar(lista, valores, color='red')
plt.title('Apple Products Prices')
plt.xlabel('Products')
plt.ylabel('Price ($)')
plt.legend(['Price'])
plt.show()
