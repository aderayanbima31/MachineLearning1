import pandas

import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/conordewey3/Hitchhikers-Guide-Machine-Learning/master/iris_df.csv"

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

dataset.plot(kind='box', subplots=True , layout=(2,2), sharex=False, sharey=False)

plt.show()